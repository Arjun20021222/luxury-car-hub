from django.urls import path
from . import views

urlpatterns = [
    path("",views.car_list,name="car_list"),
    path("<int:pk>/",views.car_detail,name="car_detail"),
    path("<int:pk>/book/",views.book_car,name="book_car"),
    path("my_bookings/",views.my_bookings,name="my_bookings"),
]
