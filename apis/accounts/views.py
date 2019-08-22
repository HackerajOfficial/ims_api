from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from apis.accounts.serializer import UserSerializer
from rest_framework import permissions

class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
