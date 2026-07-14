from django.urls import path
from .views import CarViewSet,StudentApiView,RegisterApiView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

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
urlpatterns=[
    path("student/",StudentApiView.as_view(),name="api_student"),
    path("register/",RegisterApiView.as_view(),name="api-register"),
    path("login/",TokenObtainPairView.as_view(),name="api-login"),
]

urlpatterns += router.urls