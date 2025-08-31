from django.urls import path, include
from .views import get_city

urlpatterns = [
    path("weather/",get_city, name="get_city"),
]