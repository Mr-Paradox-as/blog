from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCommentOwner


# Create your views here.
from rest_framework import generics
from .models import Post,Comment
from .serializers import PostSerializer
from .permissions import IsOwnerOnlyRead
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User # If used custom user model

from .serializers import RegisterSerializer,CommentSerializer,UserCommentSerializer


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

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
    permission_classes = [IsAuthenticated, IsCommentOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsCommentOwner]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = generics.get_object_or_404(Post, pk=post_id)
        serializer.save(user=self.request.user, post=post)

class UserCommentListView(generics.ListAPIView):
    serializer_class = UserCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(user=user)

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsCommentOwner]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
