from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import MainUserViewset
routs = DefaultRouter()
routs.register(r"registration", MainUserViewset, basename='mainuserregistration')

urlpatterns = [
    path("", include(routs.urls)),
]
