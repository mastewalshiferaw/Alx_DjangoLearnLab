from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    

    #  "books/create" 
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # "books/update"
    
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    #  "books/delete" 
    # The <int:pk> part is necessary to know which book to delete.
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]