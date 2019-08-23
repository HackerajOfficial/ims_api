
from django.urls import path
from apis.customer import views


urlpatterns = [
    path("add/",views.AddCustomerAPIView.as_view()),
    path("update/<int:pk>/",views.UpdateCustomerAPIView.as_view()),
    path("",views.ListCustomerAPIView.as_view()),
    path("delete/<int:pk>/",views.DeleteCustomerAPIView.as_view()),
]
