import django_filters
from apps.capital.models import Capital, MoneyRecord


class CapitalFilter(django_filters.rest_framework.FilterSet):
    # sort = django_filters.OrderingFilter(fields=('date_joined',))
    # min_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='gte')
    # max_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='lte')
    class Meta:
        model = Capital
        fields = ['capital_id', 'user']


class MoneyRecordTasksFilter(django_filters.rest_framework.FilterSet):
    # sort = django_filters.OrderingFilter(fields=('date_joined',))
    # min_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='gte')
    # max_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='lte')
    class Meta:
        model = MoneyRecord
        fields = ['record_id', 'user']

