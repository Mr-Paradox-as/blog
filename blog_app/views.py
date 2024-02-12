from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions

# Create your views here.
from rest_framework import generics
from .models import Post,Comment
from .serializers import PostSerializer
from .permissions import IsOwnerOnlyRead
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User # If used custom user model

from .serializers import RegisterSerializer,CommentSerializer


class CreateUserView(CreateAPIView):

    model = User()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = RegisterSerializer



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOnlyRead]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOnlyRead]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOnlyRead]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
