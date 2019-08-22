from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from apis.customer.serializer import CustomerSerializer
from common.permissions import IsAdminOrStaff
from apis.customer.models import Customer
from rest_framework_simplejwt import authentication
from common.pagination import CustomerAndSupplierPaginator


class AddCustomerAPIView(CreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminOrStaff]


class UpdateCustomerAPIView(UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAdminOrStaff]

class ListCustomerAPIView(ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAdminOrStaff]
    pagination_class = CustomerAndSupplierPaginator