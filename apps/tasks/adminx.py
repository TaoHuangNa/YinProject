import xadmin
from apps.tasks.models import Tasks, CompleteTasks, Banner, ImageInfo, Transfer


# class TasksTypeAdmin(object):
#     # 显示的列
#     list_display = ['type', "price", "complete_price"]
#     # 搜索的字段，不要添加时间搜索
#     search_fields = ['type']
#     # 过滤
#     list_filter = ['type_id', 'type']
#     ordering = ('-add_time',)
#
#
# xadmin.site.register(TasksType, TasksTypeAdmin)


class TasksAdmin(object):
    # 显示的列
    list_display = ['tasks_id', 'url', "target_times", "completed_times", "tasks_name", "cost", "complete_cost",
                    "total_cost", "state", "type", "created", "add_time", "remarks"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['tasks_id', 'state', 'created', 'completed_times', 'type']
    # 过滤
    list_filter = ['tasks_id', 'state', 'created', 'completed_times', 'type', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(Tasks, TasksAdmin)


class CompleteTasksAdmin(object):
    # 显示的列
    list_display = ['execute_id', 'tasks_id', 'image', "complete_user", "state", "remarks", "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['execute_id', 'tasks_id', "complete_user", "state"]
    # 过滤
    list_filter = ['execute_id', 'tasks_id', "complete_user", "state", 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(CompleteTasks, CompleteTasksAdmin)


class BannerAdmin(object):
    # 显示的列
    list_display = ['image', 'index', "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['image', 'index']
    # 过滤
    list_filter = ['image', 'index', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(Banner, BannerAdmin)


class ImageInfoAdmin(object):
    # 显示的列
    list_display = ['id', 'url', "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['id']
    # 过滤
    list_filter = ['id', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(ImageInfo, ImageInfoAdmin)


class TransferInfoAdmin(object):
    # 显示的列
    list_display = ['transfer_id', 'tasks_id', "money", "cheques_account", "cheques_name", "payment_account",
                    "payment_name", "image", "state", "remarks", "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['transfer_id', "tasks_id", "cheques_account", "payment_account", "state"]
    # 过滤
    list_filter = ['transfer_id', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(Transfer, TransferInfoAdmin)
