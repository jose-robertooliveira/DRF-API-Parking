from djapi.views import ParkingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', ParkingViewSet)
urlpatterns = router.urls
