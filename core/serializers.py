from rest_framework import serializers
from .models import User
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer




class UserSerializer(serializers.ModelSerializer):
    class Meta():
        fields = ['id', 'username', 'email', "password"]
       
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username','email', 'password']
        extra_kwargs = {"password": {'write_only' : True}}
# 
# class UserSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         fields = ['id', 'username', 'email', 'first_name', 'last_name']
        