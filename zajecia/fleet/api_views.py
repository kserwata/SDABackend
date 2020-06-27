from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer
from .paginators import CustomPaginator


class CarApiViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = CustomPaginator

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.query_params.get('petrol'):
            qs = qs.filter(petrol=self.request.query_params['petrol'])
        return qs
