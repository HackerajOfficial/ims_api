from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt import authentication
from apis.sales.serializer import SalesSerializer
from common.permissions import IsAdminOrStaff



class AddSalesAPIView(CreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = SalesSerializer
    permission_classes = [IsAdminOrStaff]