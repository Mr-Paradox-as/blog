from django.urls import path
from blog_app.views import PostList, PostDetail,UserList,UserDetail,CreateUserView,CommentDetailView,CommentListCreateView,PostListCreateView,UserCommentListView
from django.contrib.auth.models import User

urlpatterns = [
    path('create-post/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('users/', UserList.as_view(), name='user-list' ),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('register/', CreateUserView.as_view(model = User), name='user-list' ),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('user/comments/', UserCommentListView.as_view(), name='user-comment-list'), 
]
