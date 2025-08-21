from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed, name='user-feed'),
    path("post/<int:post_id>/like/", views.like_post, name="like_post"),
    path("post/<int:post_id>/unlike/", views.unlike_post, name="unlike_post"),

    path("<int:post_id>/like/", views.like_post, name="like_post"),
    path("<int:post_id>/unlike/", views.unlike_post, name="unlike_post"),

]

