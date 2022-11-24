from django.urls import path
from . import views


urlpatterns = [
    path('', views.UserList.as_view(), name='user_list'),
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('users/<int:pk>/posts/', views.UserPostList.as_view(), name='user_post_list'),
    path('users/<int:user_id>/posts/<int:pk>/', views.UserPostDetail.as_view(), name='user_post_detail'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'), 
]