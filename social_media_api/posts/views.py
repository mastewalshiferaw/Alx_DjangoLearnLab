from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Like
from .serializers import PostSerializer
from django.contrib.auth.decorators import login_required
from notifications.models import Notification
from django.http import HttpResponseForbidden


class PostPagination(PageNumberPagination):
    page_size = 5


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.author == request.user

# ViewSet for managing posts
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")  
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]  # Allow search
    search_fields = ['title', 'content']     
    pagination_class = PostPagination

   
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# ViewSet for managing comments
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at") 
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def feed_view(request):
    
    
    following_users = request.user.following.all()  

    feed_posts = Post.objects.filter(author__in=following_users).order_by("-created_at")  

    serializer = PostSerializer(feed_posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Prevent duplicate likes
    if Like.objects.filter(post=post, user=request.user).exists():
        return HttpResponseForbidden("You already liked this post.")

    # Create like
    Like.objects.create(post=post, user=request.user)

    # notification (don’t notify yourself)
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            content_type=ContentType.objects.get_for_model(Post),
            object_id=post.id,
        )

    return redirect("post_detail", post_id=post.id)


@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    
    Like.objects.filter(post=post, user=request.user).delete()

    return redirect("post_detail", post_id=post.id)