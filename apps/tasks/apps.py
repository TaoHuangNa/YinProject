from django.apps import AppConfig


class TasksConfig(AppConfig):
    name = 'apps.tasks'
    # app名字后台显示中文
    verbose_name = "任务管理"
