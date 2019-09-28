from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from apis.purchase.serializer import StockSerializer, PurchaseSerializer
from rest_framework_simplejwt import authentication
from common.permissions import IsAdminOrStaff
from apis.purchase.models import StockDetails, Purchase
from common.pagination import CustomerAndSupplierPaginator
from rest_framework.views import APIView


class AddStockDetailsAPIView(CreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = StockSerializer
    permission_classes = [IsAdminOrStaff]


class UpdateStockDetailsAPIView(UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = StockSerializer
    queryset = StockDetails
    permission_classes = [IsAdminOrStaff]


class DeleteStockDetailsAPIView(DestroyAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = StockSerializer
    queryset = StockDetails.objects.all()
    permission_classes = [IsAdminOrStaff]


class ListStockDetailsAPIView(ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = StockSerializer
    queryset = StockDetails.objects.all()
    permission_classes = [IsAdminOrStaff]
    pagination_class = CustomerAndSupplierPaginator


class AddPurchaseAPIView(CreateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = PurchaseSerializer
    permission_classes = [IsAdminOrStaff]


class UpdatePurchaseAPIView(UpdateAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = PurchaseSerializer
    queryset = Purchase
    permission_classes = [IsAdminOrStaff]


class ListPuchaseAPIView(ListAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    permission_classes = [IsAdminOrStaff]


class DeletePuchaseAPIView(DestroyAPIView):
    authentication_classes = [authentication.JWTAuthentication]
    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    permission_classes = [IsAdminOrStaff]




