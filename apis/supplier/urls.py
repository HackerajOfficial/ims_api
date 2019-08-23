
from django.urls import path
from apis.supplier import views


urlpatterns = [
    path("add/",views.AddSupplierAPIView.as_view()),
    path("update/<int:pk>/",views.UpdateSupplierAPIView.as_view()),
    path("",views.ListSupplierAPIView.as_view()),
    path("delete/<int:pk>/",views.DeleteSupplierAPIView.as_view()),
]
