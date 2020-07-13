from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'apps.news'
    # app名字后台显示中文
    verbose_name = "新闻公告"
