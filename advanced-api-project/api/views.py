from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions

from .models import Book, Author
from .serializers import BookSerializer
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class WelcomeAPIView(APIView):
    """
    A simple view to welcome users to the API root.
    Provides information and links to the main API endpoints.
    """
    def get(self, request, *args, **kwargs):
        # This is the data that will be returned as JSON
        welcome_message = {
            "message": "Welcome to the Advanced Book API!",
            "description": "This is the root of an API for managing books and authors.",
            "api_endpoints": {
                "list_books": "/api/books/",
                "list_authors": "/api/authors/"
            },
            "documentation": "Please see the project README for more details on filtering, searching, and ordering."
        }


class BookListView(generics.ListAPIView):
    """
    View to list all books or create a new book.
    - GET /api/books/: Returns a list of all books.
    - POST /api/books/: Creates a new book.

    Permissions:
    - Allows anyone to view the list of books (read-only).
    - Requires authentication to create a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # No need to add filter_backends if configured in settings.py

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    


class BookDetailView(generics.RetrieveAPIView):
    """
    Handles GET requests to retrieve a single Book instance by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Handles POST requests to create a new Book instance. 
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated] # Changed to IsAuthenticated for clarity

class BookUpdateView(generics.UpdateAPIView):
    """
    Handles PUT/PATCH requests to update an existing Book instance.Authentication required
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Handles DELETE requests to remove an existing Book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



# We will also create views for the Author model for completeness.

class AuthorListCreateView(generics.ListCreateAPIView):
    """
    View to list all authors or create a new one.
    - GET /api/authors/: Returns a list of all authors.
    - POST /api/authors/: Creates a new author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a single author by ID.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]