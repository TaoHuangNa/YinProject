from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'apps.users'
    # app名字后台显示中文
    verbose_name = "用户管理"
