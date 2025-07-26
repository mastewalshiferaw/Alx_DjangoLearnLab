from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth import views as auth_views

urlpatterns = [
  
  path('book/add/', views.book_add, name='book_add'),
  path('book/<int:pk>/edit/', views.book_edit, name='book_edit'),
  path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
  path('register/', views.register, name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian-dashboard/', views.librarian_view, name='librarian_view'),
    path('member-dashboard/', views.member_view, name='member_view'),

  
    path('books/', views.list_all_books, name='list_books'),
  path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

  path('add_book/', views.book_add, name='book_add'),

    
  path('edit_book/<int:pk>/', views.book_edit, name='book_edit'),

  
  path('delete_book/<int:pk>/', views.book_delete, name='book_delete'),]