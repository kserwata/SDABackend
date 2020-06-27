from django.urls import path
from .views import WidokFormularza, ApiView


urlpatterns = [
    path('', WidokFormularza.as_view(), name="fleet_list"),
    path('api', ApiView.as_view(), name='fleet_api')
]
