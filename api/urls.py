from django.urls import path
from .views import CarViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(
    "cars",
    CarViewSet,
    basename="cars"
)

urlpatterns = router.urls


# urlpatterns = [
#     path("cars/",CarListAPIView.as_view(),name="api_cars"),
# ]
