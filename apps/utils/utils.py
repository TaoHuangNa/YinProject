from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    """用户分页的公共类"""
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 10000
