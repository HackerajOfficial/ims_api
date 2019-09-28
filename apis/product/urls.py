from django.urls import path
from apis.product import views


urlpatterns = [
    path("",views.ListProductAPIView.as_view()),
]
