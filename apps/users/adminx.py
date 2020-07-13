import xadmin
from xadmin import views
from apps.users.models import VerifyCode, Member, HomeData


class BaseSetting(object):
    # 添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 全局配置，后台管理标题和页脚
    site_title = "后台管理"
    site_footer = "Copyright 2020 by Tao Huang"
    # 菜单收缩
    # menu_style = "accordion"


class MobileVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'mobile', "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'mobile']
    # 过滤
    list_filter = ['code', 'mobile', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(VerifyCode, MobileVerifyRecordAdmin)


class MemberAdmin(object):
    # 显示的列
    list_display = ['member_id', 'member_name', "common_num", "member_num", "time", "place", "time_type", "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['member_id', 'member_name']
    # 过滤
    list_filter = ['member_id', 'member_name', 'add_time']
    ordering = ('-add_time',)


class HomeDataAdmin(object):
    # 显示的列
    list_display = ['id', 'tasks_today', "user_today", "complete", "goal", "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['id', 'add_time']
    # 过滤
    list_filter = ['id', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(Member, MemberAdmin)
xadmin.site.register(HomeData, HomeDataAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

