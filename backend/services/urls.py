from django.urls import path
from . import views

urlpatterns = [
    path("", views.service_list, name="service_list"),

    path("floor1/", views.floor1, name="floor1"),
]