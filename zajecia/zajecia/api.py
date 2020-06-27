from rest_framework import routers
from fleet.api_views import CarApiViewset


router = routers.DefaultRouter()
router.register(r'fleet', CarApiViewset)
