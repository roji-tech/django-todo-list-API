from rest_framework import serializers
from .models import User
# from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer



class UserCreateSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ["id", 'first_name', 'last_name', "email", "username", "password"]
      # fields = "-_all-_"
      extra_kwargs = {"password": {'write_only' : True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
# class UserCreateSerializer(BaseUserCreateSerializer):
#     class Meta(BaseUserCreateSerializer.Meta):
#         fields = ['id', 'username', 'password',
#                   'email', 'first_name', 'last_name']
# 
# class UserSerializer(BaseUserSerializer):
#     class Meta(BaseUserSerializer.Meta):
#         fields = ['id', 'username', 'email', 'first_name', 'last_name']
        