from django.urls import path
from apis.category import views


urlpatterns = [
    path("",views.ListCategoryAPIView.as_view()),
]
