from django.urls import path
from .views import BookListCreateView, BookDetailView, AuthorListCreateView, AuthorDetailView

# --- Documentation for URL Patterns ---
# The URL patterns map specific HTTP endpoints to the views we defined.


urlpatterns = [
    # Book URLs
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Author URLs
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]