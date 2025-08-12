from django.urls import path
# We import Django's built-in views for login and logout
from django.contrib.auth import views as auth_views
from . import views 

urlpatterns = [
    # Path for our custom registration view
    path('register/', views.register, name='register'),

    # Path for Django's built-in LoginView.
    
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Path for  LogoutView.
    
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Path for custom profile view
    path('profile/', views.profile, name='profile'),
]