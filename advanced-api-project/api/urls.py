from django.urls import path

from .views import BookListCreateAPIView, BookDetailUpdateDeleteAPIView



urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailUpdateDeleteAPIView.as_view(), name='book-detail-update-delete'),
]