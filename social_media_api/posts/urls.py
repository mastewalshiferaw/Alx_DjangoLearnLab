from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed_view, like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    
    path('', include(router.urls)),

    path('feed/', feed_view, name='user-feed'),
    path("<int:pk>/like/", like_post, name="like_post"),
    path("<int:pk>/unlike/", unlike_post, name="unlike_post"),
]
