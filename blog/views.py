from .serializer import UserSerializer, PostSerializer
from rest_framework import generics
from .models import User, Post

# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'blog/user_list.html', {'users': users})

# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})
