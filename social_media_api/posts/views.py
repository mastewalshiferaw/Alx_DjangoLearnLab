from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets, filters, permissions
from rest_framework.pagination import PageNumberPagination

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from rest_framework import generics  # for generics.get_object_or_404
from django.contrib.contenttypes.models import ContentType

from .models import Post, Like, Comment
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification



# Pagination for PostViewSet
class PostPagination(PageNumberPagination):
    page_size = 5



class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only requests are allowed
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise only author can modify
        return obj.author == request.user



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]  # Allow search
    search_fields = ['title', 'content']
    pagination_class = PostPagination

    def perform_create(self, serializer):
        # Automatically set the author to the requesting user
        serializer.save(author=self.request.user)



# ViewSet for Comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def feed_view(request):
    following_users = request.user.following.all()  # assumes 'following' ManyToMany
    feed_posts = Post.objects.filter(author__in=following_users).order_by("-created_at")
    serializer = PostSerializer(feed_posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



# Like post view
@login_required
def like_post(request, pk):
   
    post = generics.get_object_or_404(Post, pk=pk)  # matches expected pattern

    # Prevent duplicate likes
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return HttpResponseForbidden("You already liked this post.")

    # Create notification for the post author (not for self-likes)
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(Post),
            object_id=post.id,
        )

    return redirect("post_detail", pk=post.pk)



# Unlike post view
@login_required
def unlike_post(request, pk):
    """
    Handle unliking a post:
    - Removes the like if it exists
    """
    post = generics.get_object_or_404(Post, pk=pk)
    Like.objects.filter(user=request.user, post=post).delete()
    return redirect("post_detail", pk=post.pk)
