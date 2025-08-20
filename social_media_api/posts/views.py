from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

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