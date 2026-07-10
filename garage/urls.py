from django.urls import path
from .import views


urlpatterns=[
    path("book/",views.book_service,name="book_service"),
    path("my_services/",views.my_services,name="my_services"),
]