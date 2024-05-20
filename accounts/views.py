from django.shortcuts import render
from .models import MainUser
from .serializers import MainUserSrializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# Create your views here.

class MainUserViewset(ModelViewSet):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSrializers