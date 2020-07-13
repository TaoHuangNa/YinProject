"""YinProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

from apps.tasks.views import TasksViewSet, CompleteTasksViewSet, BannerViewSet, ImageInfoViewSet, \
    HomePageViewSet, MyTasksViewSet, TransferViewSet, CheckTasksViewSet, CheckCompleteTasksViewSet, \
    CheckMemberTasksViewSet, OpenMemberViewSet
from apps.capital.views import CapitalViewSet, MoneyRecordViewSet
from apps.news.views import NewsViewSet, NoticeViewSet
from apps.users.views import UserProfileViewSet, MemberViewSet, SmsCodeViewSet, UserRegViewSet, PasswordResetViewSet, \
    UserBalanceViewSet, PasswordUpdateViewSet, TeamViewSet, HomeDataViewSet

router = routers.DefaultRouter()
# 任务信息view注册
router.register('tasks', TasksViewSet, base_name="tasks")
# 任务类型view注册
# router.register('tasks_type', TasksTypeViewSet, base_name="tasks_type")
# 完成任务信息view注册
router.register('complete_tasks', CompleteTasksViewSet, base_name="complete_tasks")
# 轮播图view注册
router.register('banner', BannerViewSet, base_name="banner")
# 资金信息view注册
router.register('capital', CapitalViewSet, base_name="capital")
# 提现记录view注册
router.register('money_record', MoneyRecordViewSet, base_name="money_record")
# 用户信息view注册
router.register('user', UserProfileViewSet, base_name="user")
# 会员信息view注册
router.register('member', MemberViewSet, base_name="member")
# 验证码view注册
router.register('verify', SmsCodeViewSet, base_name="verify")
# 用户注册view注册
router.register('register', UserRegViewSet, base_name="register")
# 用户密码修改view注册
router.register('reset_password', PasswordResetViewSet, base_name="reset_password")
# 新闻公告view注册
router.register('news', NewsViewSet, base_name="news")
# 图片view注册
router.register('image', ImageInfoViewSet, base_name="image")
# 首页数据view注册
# router.register('homepage', HomePageViewSet, base_name="homepage")
router.register('homepage', HomeDataViewSet, base_name="homepage")
# 用户金额信息
router.register('user_balance', UserBalanceViewSet, base_name="user_balance")
# 用户金额信息
router.register('update_password', PasswordUpdateViewSet, base_name="update_password")
# 用户团队信息
router.register('team', TeamViewSet, base_name="team")
# 自己操作自己创建的任务
router.register('my_tasks', MyTasksViewSet, base_name="my_tasks")
# 通知信息
router.register('notice', NoticeViewSet, base_name="notice")
# 支付信息
router.register('transfer', TransferViewSet, base_name="transfer")
# 展示任务审核信息
router.register('check_tasks', CheckTasksViewSet, base_name="check_tasks")
# 展示完成任务审核信息
router.register('check_complete_tasks', CheckCompleteTasksViewSet, base_name="check_complete_tasks")
# 展示开通会员审核信息
router.register('check_member', CheckMemberTasksViewSet, base_name="check_member")
# 开通会员审核信息
router.register('open_member', OpenMemberViewSet, base_name="open_member")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('jwt-auth/', obtain_jwt_token),
    # rest_framework用户验证
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # 接口API说明文档
    path('docs/', include_docs_urls(title='API接口'), name="docs_old"),
    path('api/docs/', get_swagger_view(title="API接口"), name="docs"),
    # 接口API部分URL
    path('api/', include(router.urls)),

]
