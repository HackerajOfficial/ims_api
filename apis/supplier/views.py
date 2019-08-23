from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from apis.supplier.serializer import SupplierSerializer
from common.permissions import IsAdminOrStaff
from apis.supplier.models import Supplier
from rest_framework_simplejwt import authentication
from common.pagination import CustomerAndSupplierPaginator


class AddSupplierAPIView(CreateAPIView):
    serializer_class = SupplierSerializer
    permission_classes = [IsAdminOrStaff]


class UpdateSupplierAPIView(UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAdminOrStaff]


class ListSupplierAPIView(ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAdminOrStaff]
    pagination_class = CustomerAndSupplierPaginator


class DeleteSupplierAPIView(DestroyAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsAdminOrStaff]
