from rest_framework import serializers
from login.models import LoginUser


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=LoginUser
        fields=('username','password')
