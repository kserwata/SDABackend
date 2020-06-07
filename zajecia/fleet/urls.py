from django.urls import path
from .views import WidokFormularza


urlpatterns = [
    path('', WidokFormularza.as_view(), name="fleet_list")
]
