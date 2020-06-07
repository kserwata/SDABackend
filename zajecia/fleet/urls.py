from django.urls import path
from .views import FleetView


urlpatterns = [
    path('', FleetView.as_view(), name="fleet_list")
]
