import django_filters
from apps.users.models import UserProfile, Member


class UserProfileFilter(django_filters.rest_framework.FilterSet):
    # sort = django_filters.OrderingFilter(fields=('date_joined',))
    # min_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='gte')
    # max_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='lte')
    class Meta:
        model = UserProfile
        fields = ['invitation_name', 'username']


class MemberTasksFilter(django_filters.rest_framework.FilterSet):
    # sort = django_filters.OrderingFilter(fields=('date_joined',))
    # min_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='gte')
    # max_date = django_filters.DateFilter(name='date_joined__date', lookup_expr='lte')
    class Meta:
        model = Member
        fields = ['member_id', 'member_name']
