from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.news.models import News, Notice
from apps.news.serializers import NewsModelsSerializer, NoticeModelsSerializer
from apps.utils.utils import Pagination


class NewsViewSet(viewsets.ModelViewSet):
    """
    create: 新闻公告 - 新增新闻公告
    list: 新闻公告 - 查询多笔新闻公告
    retrieve: 新闻公告 - 查询单条新闻公告
    update: 新闻公告 - 更新新闻公告（覆盖更新模式）
    partial_update: 新闻公告 - 更新新闻公告（部分更新模式）
    delete: 新闻公告 - 删除新闻公告
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = News.objects.all().order_by('-add_time')
    serializer_class = NewsModelsSerializer
    lookup_field = 'new_id'
    pagination_class = Pagination


class NoticeViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    list: 通知 - 查询多笔通知
    """
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Notice.objects.all().order_by('-add_time')
    serializer_class = NoticeModelsSerializer
    lookup_field = 'notice_id'
    pagination_class = Pagination



