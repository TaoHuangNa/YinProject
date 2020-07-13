from decimal import Decimal
import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import F, Q
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.tasks.models import Tasks, CompleteTasks, Banner, ImageInfo, Transfer
from apps.tasks.serializers import TasksModelsSerializer, CompleteTasksModelsSerializer, BannerModelsSerializer, \
    CompleteTasksCreateModelsSerializer, ImageInfoModelsSerializer, HomePageModelsSerializer, MyTasksModelsSerializer, \
    TransferModelsSerializer, CheckTasksModelsSerializer, CheckCompleteTasksModelsSerializer, \
    CheckMemberModelsSerializer
from apps.utils.utils import Pagination
from apps.tasks.filters import TasksFilter, CompleteTasksFilter
from apps.capital.models import Capital
from apps.users.models import UserProfile


class TasksViewSet(viewsets.ModelViewSet):
    """
    create: 任务信息 - 新增任务信息
    list: 任务信息 - 查询多笔任务信息
    retrieve: 任务信息 - 查询单条任务信息
    update: 任务信息 - 更新任务信息（覆盖更新模式）
    partial_update: 任务信息 - 更新任务信息（部分更新模式）
    delete: 任务信息 - 删除任务信息
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Tasks.objects.all().order_by('-add_time')
    serializer_class = TasksModelsSerializer
    lookup_field = 'tasks_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = TasksFilter

    def get_queryset(self):
        if not self.request.user.is_staff:
            tasks_id_list = CompleteTasks.objects.filter(complete_user=self.request.user, state__in=["0", "2"]).values_list('tasks_id')
            # gt/gte/lt/lte——对应于>,>=,<,<=   F比较model内部字段
            # 不返回：任务次数<=完成次数和已经做过得任务,进行中
            a = Tasks.objects.exclude(Q(target_times__lte=F('completed_times')) | Q(tasks_id__in=tasks_id_list) | Q(state__in=["0", "1", "3", "4", "5"])).order_by('-add_time')
            # a = Tasks.objects.exclude(target_times__lte=F('completed_times')).order_by('-add_time')
            return a
        else:
            return Tasks.objects.all()


class CompleteTasksViewSet(viewsets.ModelViewSet):
    """
    create: 任务完成信息 - 新增任务完成信息
    list: 任务完成信息 - 查询多笔任务完成信息
    retrieve: 任务完成信息 - 查询单条任务完成信息
    update: 任务完成信息 - 更新任务完成信息（覆盖更新模式）
    partial_update: 任务完成信息 - 更新任务完成信息（部分更新模式）
    delete: 任务完成信息 - 删除任务完成信息
    """
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = CompleteTasks.objects.all().order_by('-add_time')
    serializer_class = CompleteTasksModelsSerializer

    lookup_field = 'execute_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CompleteTasksFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # # 创建完成任务的时候，任务完成条数增加1
        # completed_times = Tasks.objects.filter(tasks_id=request.data["tasks_id"]).values('completed_times')[0]['completed_times']
        # completed_times = completed_times + 1
        # Tasks.objects.filter(tasks_id=request.data["tasks_id"]).update(completed_times=completed_times)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        if 'state' in request.data.keys():
            # 审核状态为1.不通过, 任务完成条完成次数-1,
            if request.data["state"] == "1":
                tasks_id = CompleteTasks.objects.filter(execute_id=kwargs["execute_id"]).values("tasks_id")[0]["tasks_id"]
                completed_times = Tasks.objects.filter(tasks_id=tasks_id).values('completed_times')[0][
                    'completed_times']
                completed_times = completed_times - 1
                Tasks.objects.filter(tasks_id=tasks_id).update(completed_times=completed_times)
            elif request.data["state"] == "2":
                # 添加资金明细 ，和修改用户的余额、任务奖励
                complete_data = CompleteTasks.objects.filter(execute_id=kwargs["execute_id"]).values("complete_user", "price", "state", "tasks_id")[0]
                # 判断原始状态,如果原始状态为已完成，不进行处理
                if complete_data["state"] != "2":
                    Capital.objects.create(user=complete_data["complete_user"], money=complete_data["price"], type="0", operation="任务奖励")
                    # 获取完成者的用户信息
                    user = UserProfile.objects.filter(username=complete_data["complete_user"])
                    user_data = user.values("balance", "task_reward", "invitation_name", "member_level")[0]
                    balance, task_reward = user_data["balance"], user_data["task_reward"]
                    # 完成者的用户信息中的余额和任务奖励都加上余额
                    balance = balance + complete_data["price"]
                    task_reward = task_reward + complete_data["price"]
                    user.update(balance=balance, task_reward=task_reward)
                    # 任务类型
                    task_type = Tasks.objects.filter(tasks_id=complete_data["tasks_id"]).values("type")[0]["type"]
                    # 判断任务类型和用户是否会员 如果是会员任务并且是会员，则给增加上级提成
                    if task_type == "1" and user_data["member_level"] != "1":
                        invitation_name = user_data["invitation_name"]
                        Capital.objects.create(user=invitation_name, money=complete_data["price"] * Decimal(0.1),
                                               type="0", operation="团队收益")
                        invitation_user = UserProfile.objects.filter(username=invitation_name)
                        invitation_user_data = invitation_user.values("balance", "task_reward")[0]
                        balance, team_income = invitation_user_data["balance"], invitation_user_data["task_reward"]
                        # 邀请者的用户信息中的余额和团队收益都加上余额
                        balance = balance + complete_data["price"] * Decimal(0.1)
                        team_income = team_income + complete_data["price"] * Decimal(0.1)
                        invitation_user.update(balance=balance, team_income=team_income)
                        print(invitation_name)
            else:
                pass
        return self.update(request, *args, **kwargs)

    # def get_queryset(self):
    #     return CompleteTasks.objects.filter(complete_user=self.request.user).order_by('-add_time')

    # 根据请求类型不同，设置不同的序列化器
    def get_serializer_class(self):
        if self.action in ("create"):
            return CompleteTasksCreateModelsSerializer
        else:
            return CompleteTasksModelsSerializer


class BannerViewSet(viewsets.ModelViewSet):
    """
    create: 首页轮播的图片 - 新增首页轮播的图片
    list: 首页轮播的图片 - 查询多笔首页轮播的图片
    retrieve: 首页轮播的图片 - 查询首页轮播的图片
    update: 首页轮播的图片 - 更新首页轮播的图片（覆盖更新模式）
    partial_update: 首页轮播的图片 - 更新首页轮播的图片（部分更新模式）
    delete: 首页轮播的图片 - 删除首页轮播的图片
    """
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)

    queryset = Banner.objects.all().order_by('-add_time')
    serializer_class = BannerModelsSerializer

    lookup_field = 'index'


class ImageInfoViewSet(viewsets.ModelViewSet):
    """
    create: 图片 - 新增图片
    list: 图片 - 查询图片
    retrieve: 图片 - 查询图片
    update: 图片 - 更新图片（覆盖更新模式）
    partial_update: 图片 - 更新图片（部分更新模式）
    delete: 图片 - 删除图片
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = ImageInfo.objects.all().order_by('-add_time')
    serializer_class = ImageInfoModelsSerializer

    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class HomePageViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list: 获取首页数据： 今日任务数、今日用户数、今日已完成
    """
    # authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    # permission_classes = (IsAuthenticated,)

    serializer_class = HomePageModelsSerializer

    def get_queryset(self):
        return [1]


class MyTasksViewSet(viewsets.ModelViewSet):
    """
    list: 获取自己创建的任务
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    serializer_class = MyTasksModelsSerializer

    def get_queryset(self):
        return Tasks.objects.filter(created=self.request.user)

    lookup_field = 'tasks_id'
    pagination_class = Pagination


class TransferViewSet(mixins.CreateModelMixin, GenericViewSet):
    """
    create: 新增支付信息
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Banner.objects.all().order_by('-add_time')
    serializer_class = TransferModelsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        if not request.data["member"]:
            Tasks.objects.filter(tasks_id=request.data["tasks_id"]).update(state="1")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CheckTasksViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list: 获取未审核的任务
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Tasks.objects.filter(state='1').order_by('-add_time')
    serializer_class = CheckTasksModelsSerializer
    lookup_field = 'tasks_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = TasksFilter


class CheckCompleteTasksViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list: 获取未审核的完成的任务
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = CompleteTasks.objects.filter(state='0').order_by('-add_time')
    serializer_class = CheckCompleteTasksModelsSerializer
    lookup_field = 'execute_id'
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filter_class = CompleteTasksFilter


class CheckMemberTasksViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list: 获取未审核的开通会员
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Transfer.objects.filter(state='0', member=True).order_by('-add_time')
    serializer_class = CheckMemberModelsSerializer
    lookup_field = 'transfer_id'
    pagination_class = Pagination


class OpenMemberViewSet(UpdateModelMixin, viewsets.GenericViewSet):
    """开通会员审核"""
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = TransferModelsSerializer
    queryset = Transfer.objects.filter(state='0', member=True)
    # queryset = Transfer.objects.filter( member=True)
    lookup_field = 'transfer_id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        if request.data["state"] == "1":
            # 审核通过
            # 获取用户
            created = Transfer.objects.filter(transfer_id=kwargs["transfer_id"]).values("created")[0]["created"]
            if request.data["time_type"] == "0":
                # 期限类型为天
                time = (datetime.date.today() + relativedelta(days=+1)).strftime('%Y%m%d')
            elif request.data["time_type"] == "1":
                # 期限类型为月
                time = (datetime.date.today() + relativedelta(months=+1)).strftime('%Y%m%d')
            elif request.data["time_type"] == "2":
                time =(datetime.date.today() + relativedelta(years=+1)).strftime('%Y%m%d')
            else:
                # 默认为月
                time = (datetime.date.today() + relativedelta(months=+1)).strftime('%Y%m%d')
            UserProfile.objects.filter(username=created).update(member_limit=time, member_level=request.data["tasks_id"])
        return self.update(request, *args, **kwargs)
