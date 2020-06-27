from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math


class CustomPaginator(PageNumberPagination):
    page_size_query_param = 'size'

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'items': data,
            'page_count': math.ceil(self.page.paginator.count / self.page_size)
        })
