from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetail.as_view(), name='post_detail')
    # path('', views.user_list, name='user_list'),
    # path('posts/<int:pk>', views.post_list, name='post_list')
]