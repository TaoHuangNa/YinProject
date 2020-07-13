from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.capital.models import Capital, MoneyRecord
from apps.capital.serializers import CapitalModelsSerializer, MoneyRecordTasksModelsSerializer, \
    MoneyRecordTasksUpdateModelsSerializer
from apps.utils.utils import Pagination
from apps.capital.filters import CapitalFilter, MoneyRecordTasksFilter
from apps.users.models import UserProfile


class CapitalViewSet(viewsets.ModelViewSet):
    """
    create: 资金明细 - 新增资金明细
    list: 资金明细 - 查询多笔资金明细
    retrieve: 资金明细 - 查询单条资金明细
    update: 资金明细 - 更新资金明细（覆盖更新模式）
    partial_update: 资金明细 - 更新资金明细（部分更新模式）
    delete: 资金明细 - 删除资金明细
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Capital.objects.all().order_by('-add_time')
    serializer_class = CapitalModelsSerializer
    lookup_field = 'capital_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CapitalFilter


class MoneyRecordViewSet(viewsets.ModelViewSet):
    """
    create: 提现记录 - 新增提现记录
    list: 提现记录 - 查询多条提现记录
    retrieve: 提现记录 - 查询单条提现记录
    update: 提现记录 - 更新提现记录（覆盖更新模式）
    partial_update: 提现记录 - 更新提现记录（部分更新模式）
    delete: 提现记录 - 删除提现记录
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = MoneyRecord.objects.all().order_by('-add_time')
    serializer_class = MoneyRecordTasksModelsSerializer

    lookup_field = 'record_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = MoneyRecordTasksFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        balance = request.user.balance-serializer.validated_data["money"]
        # 用户余额减少提现金额
        UserProfile.objects.filter(username=request.user).update(balance=balance)
        Capital.objects.create(user=request.user, money=serializer.validated_data["money"], type="1",
                               operation="提现")
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        if request.data['state'] == "2":
            # 审核不通过
            moneyrecord = MoneyRecord.objects.filter(record_id=kwargs["record_id"]).values("money", "user")[0]
            money, user = moneyrecord["money"], moneyrecord["user"]
            Capital.objects.create(user=request.user, money=money, type="0", operation="提现驳回")
            balance = UserProfile.objects.filter(username=user).values("balance")[0]["balance"] + money
            UserProfile.objects.filter(username=user).update(balance=balance)
        return self.update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ("'partial_update'"):
            return MoneyRecordTasksUpdateModelsSerializer
        else:
            return MoneyRecordTasksModelsSerializer
