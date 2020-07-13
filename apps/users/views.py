from decimal import Decimal
from random import choice

from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from apps.users.models import UserProfile, Member, VerifyCode, HomeData
from apps.users.serializers import UserProfileModelsSerializer, MemberModelsSerializer, VerifyCodeModelsSerializer, \
    UserRegSerializer, PasswordResetSerializer, UserBalanceModelsSerializer, PasswordUpdateSerializer, \
    TeamModelsSerializer, HomeDataModelsSerializer
from apps.utils.utils import Pagination
from apps.users.filters import UserProfileFilter, MemberTasksFilter
from apps.utils.common import send__sms
from apps.capital.models import Capital

User = get_user_model()


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    create: 用户信息 - 新增用户信息
    list: 用户信息 - 查询多笔用户信息
    retrieve: 用户信息 - 查询单条用户信息
    update: 用户信息 - 更新用户信息（覆盖更新模式）
    partial_update: 用户信息 - 更新用户信息（部分更新模式）
    delete: 用户信息 - 删除用户信息
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = UserProfile.objects.all().order_by('-date_joined')
    serializer_class = UserProfileModelsSerializer
    lookup_field = 'username'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = UserProfileFilter

    # ########################################暂时不用这个规则##########################################
    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     # 如果会员等级在请求的数据中，说明在修改会员等级，要给上级提成
    #     if 'member_level' in request.data.keys():
    #         # 开通会员的价格
    #         # 邀请人的会员等级
    #         invitation_data = UserProfile.objects.filter(username=request.data["invitation_name"]).values("member_level", "balance", "commission")[0]
    #         # 邀请人会员等级
    #         invitation_level = invitation_data["member_level"]
    #         # 邀请人余额
    #         invitation_balance = invitation_data["balance"]
    #         # 邀请人套餐提成
    #         invitation_commission = invitation_data["commission"]
    #         # 判断邀请人的会员等级是否小于开通会员的等级
    #         if request.data["member_level"] < invitation_level:
    #             place = Member.objects.filter(member_id=request.data["member_level"]).values("place")[0]["place"] * Decimal(0.18)
    #         else:
    #             # 如果大于邀请人的会员，按照邀请人的会员拿到提成
    #             place = Member.objects.filter(member_id=invitation_level).values("place")[0]["place"] * Decimal(0.18)
    #         invitation_balance = invitation_balance + place
    #         invitation_commission = invitation_commission + place
    #         Capital.objects.create(user=request.data["invitation_name"], money=place, type="0", operation="套餐提成")
    #         UserProfile.objects.filter(username=request.data["invitation_name"]).update(balance=invitation_balance,
    #                                                                                     commission=invitation_commission)
    #     return self.update(request, *args, **kwargs)


class MemberViewSet(viewsets.ModelViewSet):
    """
    create: 会员信息 - 新增会员信息
    list: 会员信息 - 查询多笔会员信息
    retrieve: 会员信息 - 查询单条会员信息
    update: 会员信息 - 更新会员信息（覆盖更新模式）
    partial_update: 会员信息 - 更新会员信息（部分更新模式）
    delete: 会员信息 - 删除会员信息
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Member.objects.exclude(member_id=1).order_by('add_time')
    serializer_class = MemberModelsSerializer

    lookup_field = 'member_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = MemberTasksFilter


class SmsCodeViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    验证码发送
    """
    queryset = VerifyCode.objects.all()
    serializer_class = VerifyCodeModelsSerializer

    def generate_code(self):
        """
        生成六位数字的验证码
        """
        seeds = "1234567890"
        random_str = []
        for i in range(6):
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # 验证合法
        serializer.is_valid(raise_exception=True)
        # 判断该手机号是否进行过注册
        mobile = serializer.validated_data["mobile"]

        # 生成验证码
        code = self.generate_code()

        code_record = VerifyCode(code=code, mobile=mobile)
        code_record.save()
        model = "SMS_194050695"
        params = {"code": code}
        sms_status = send__sms(mobile, model, params)
        # sms_status = {"Code": "OK"}
        print(code)
        if sms_status["Code"] != 'OK':
            return Response({
                "code": [sms_status["Message"]]
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'mobile': mobile}, status=status.HTTP_201_CREATED)


class UserRegViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """用户注册"""
    serializer_class = UserRegSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        # re_dict["name"] = user.name if user.name else user.username
        re_dict["username"] = user.username
        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class PasswordResetViewSet(UpdateModelMixin, viewsets.GenericViewSet):
    """用户密码修改"""
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = PasswordResetSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


class UserBalanceViewSet(ListModelMixin, viewsets.GenericViewSet):
    """获取用户今日信息"""
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = UserBalanceModelsSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(username=self.request.user)

    lookup_field = 'username'

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = UserProfileFilter


class PasswordUpdateViewSet(UpdateModelMixin, viewsets.GenericViewSet):
    """更新登陆密码"""
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = PasswordUpdateSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(username=self.request.user)

    lookup_field = 'username'

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    # filter_class = UserProfileFilter


class TeamViewSet(ListModelMixin, viewsets.GenericViewSet):
    """获取团队信息"""
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = TeamModelsSerializer
    pagination_class = Pagination

    def get_queryset(self):
        return UserProfile.objects.filter(invitation_name=self.request.user)


class HomeDataViewSet(ListModelMixin, viewsets.GenericViewSet):
    """获取首页数据"""
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = HomeData.objects.filter(id=1)
    serializer_class = HomeDataModelsSerializer
    pagination_class = Pagination

