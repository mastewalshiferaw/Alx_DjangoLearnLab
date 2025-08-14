from django.urls import path

from django.contrib.auth import views as auth_views
from . import views 
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from .views import CommentUpdateView, CommentDeleteView

urlpatterns = [
    # Path for our custom registration view
    path('register/', views.register, name='register'),

    # Path for Django's built-in LoginView.
    
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Path for  LogoutView.
    
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Path for custom profile view
    path('profile/', views.profile, name='profile'),

        # Map each view to a URL
    
    path('', PostListView.as_view(), name='post-list'), # Set the home page to list all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create')
]