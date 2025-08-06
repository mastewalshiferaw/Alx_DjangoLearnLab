from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


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