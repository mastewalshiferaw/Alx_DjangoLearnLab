from django.urls import path
from . import views 
from .views import list_books
urlpatterns = [
   
    path('books/', views.list_all_books, name='list_books'),

   
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]