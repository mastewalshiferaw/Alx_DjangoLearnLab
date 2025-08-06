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



class BookListCreateAPIView(views.APIView):
    """
    This dispatcher view is connected to the '/api/books/' endpoint.
    - If the request is GET, it dispatches to BookListView.
    - If the request is POST, it dispatches to BookCreateView.
    """
    def get(self, request, *args, **kwargs):
        return BookListView.as_view()(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return BookCreateView.as_view()(request, *args, **kwargs)

class BookDetailUpdateDeleteAPIView(views.APIView):
    """
    This dispatcher view is connected to the '/api/books/<pk>/' endpoint.
    - If the request is GET, it dispatches to BookDetailView.
    - If the request is PUT or PATCH, it dispatches to BookUpdateView.
    - If the request is DELETE, it dispatches to BookDeleteView.
    """
    def get(self, request, *args, **kwargs):
        return BookDetailView.as_view()(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return BookUpdateView.as_view()(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return BookUpdateView.as_view()(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return BookDeleteView.as_view()(request, *args, **kwargs)