from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login


def login(request):
    user = User.objects.all()
    login(request,user)
