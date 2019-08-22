from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from apis.accounts.serializer import UserSerializer
from rest_framework import permissions
from apis.accounts.models import User
from common.permissions import IsAdminOrStaff

class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UpdateUserAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminOrStaff]