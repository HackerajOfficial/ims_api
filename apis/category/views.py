from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt import authentication
from apis.category.serializer import CategorySerializer
from common.permissions import IsAdminOrStaff
from apis.category.models import Category


class ListCategoryAPIView(ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAdminOrStaff]


    
