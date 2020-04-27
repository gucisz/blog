from django.urls import path
from .views import (PostListView, PostDetailView, PostCreateView,
                    PostUpdateView, PostDeleteView, UserPostListView,
                    CommentUpdateView,CommentDeleteView, SearchResultsView)


from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment_remove'),



    path('about/', views.about, name='blog_about'),
]