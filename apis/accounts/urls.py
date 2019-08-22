from django.urls import path
from apis.accounts import views

urlpatterns = [
    path("users/",views.CreateUserAPIView.as_view()),
    path("users/<int:pk>/",views.UpdateUserAPIView.as_view()),
    # path("users/<int:pk>/delete/",views.DestroyAPIView.as_view()),
    # path("<int:pk>/news/",views.UserPosts),
]
