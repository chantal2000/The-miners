from django.shortcuts import render
from login.models import LoginUser
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class LoginViewSet(viewsets.ModelViewSet):
    queryset=LoginUser.objects.all()
    serializer_class=LoginSerializer
