import django_filters
from apps.tasks.models import Tasks, CompleteTasks


# class OrderFilter(django_filters.rest_framework.FilterSet):
#     """
#
#     """
#     # sort = django_filters.OrderingFilter(fields=('date_joined',))
#     min_date = django_filters.DateFilter(field_name='create_time__date', lookup_expr='gte', help_text="开始日期",
#                                          label="开始日期")
#     max_date = django_filters.DateFilter(field_name='create_time__date', lookup_expr='lte', help_text="截止日期",
#                                          label="截止日期")
#     min_pay = django_filters.CharFilter(field_name='pay_ratio', lookup_expr='gte', help_text="最小比例")
#     max_pay = django_filters.CharFilter(field_name='pay_ratio', lookup_expr='lte', help_text="最大比例")
#     enterprise_name = django_filters.CharFilter(field_name='own_enterprise__name', lookup_expr="icontains",
#                                                 help_text="企业名称")
#     enterprise = django_filters.CharFilter(field_name='own_enterprise__abbreviation', help_text="企业编码")
#     creator_name = django_filters.CharFilter(field_name='creator__first_name', help_text="业务员名称")
#
#     #payratio = django_filters.RangeFilter(field_name='payratio', lookup_expr='range')
#
#     class Meta:
#         model = Order
#         # fields = ['enterprise', 'lock_flag', 'lock_loan_no', 'lock_flag', 'check_state', 'order_no', 'creator',
#         #           'order_price', 'state', 'creator_name']
#         fields = {
#             'lock_flag': ['exact'],
#             'lock_loan_no': ['exact'],
#             'check_state': ['exact'],
#             'order_no': ['exact'],
#             'creator': ['exact'],
#             'order_price': ['exact'],
#             'state': ['in']
#         }


class TasksFilter(django_filters.rest_framework.FilterSet):
    # sort = django_filters.OrderingFilter(fields=('date_joined',))
    # min_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='gte')
    # max_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='lte')
    class Meta:
        model = Tasks
        fields = ['created', 'tasks_id', 'type', 'state']


class CompleteTasksFilter(django_filters.rest_framework.FilterSet):
    # sort = django_filters.OrderingFilter(fields=('date_joined',))
    # min_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='gte')
    # max_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='lte')
    class Meta:
        model = CompleteTasks
        fields = ['execute_id', 'complete_user', 'tasks_id', 'state']

