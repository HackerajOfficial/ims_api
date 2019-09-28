from django.urls import path
from apis.sales import views

urlpatterns = [
    
    # path('add_stock_details/', views.AddStockDetailsAPIView.as_view()),
    # path('edit_stock_details/<int:pk>/', views.UpdateStockDetailsAPIView.as_view()),
    # path('stock_details/delete/<int:pk>/', views.DeleteStockDetailsAPIView.as_view()),
    # path('view_stock_details/', views.ListStockDetailsAPIView.as_view()),
    path('add/', views.AddSalesAPIView.as_view()),
    # path('edit/<int:pk>/', views.UpdatePurchaseAPIView.as_view()),
    # path('', views.ListPuchaseAPIView.as_view()),
    # path('delete/<int:pk>/', views.DeletePuchaseAPIView.as_view()),

]