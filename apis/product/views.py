from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt import authentication
from apis.product.serializer import ProductSerializer
from common.permissions import IsAdminOrStaff
from apis.product.models import Product


class ListProductAPIView(ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAdminOrStaff]


    
