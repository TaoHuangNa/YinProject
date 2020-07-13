import xadmin
from apps.news.models import News, Notice


class NewsAdmin(object):
    # 显示的列
    list_display = ['new_id', 'new_title']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['new_id', 'new_title']
    # 过滤
    list_filter = ['new_id', 'new_title', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(News, NewsAdmin)


class NoticeInfoAdmin(object):
    # 显示的列
    list_display = ['notice_id', 'notice_content', "add_time"]
    # 搜索的字段，不要添加时间搜索
    search_fields = ['notice_id', "add_time"]
    # 过滤
    list_filter = ['notice_id', 'add_time']
    ordering = ('-add_time',)


xadmin.site.register(Notice, NoticeInfoAdmin)

