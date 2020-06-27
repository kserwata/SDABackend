from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer
from .paginators import CustomPaginator


class CarApiViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = CustomPaginator
