from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# --- Registration View ---
def register(request):
    # (POST request)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() # This saves to the database
            username = form.cleaned_data.get('username')
            # give the user feedback
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') # Redirect to the login page
    # If the user is just visiting the page (GET request)
    else:
        form = CustomUserCreationForm() # Create a blank instance of the form
    # Render the template, passing the form to it
    return render(request, 'blog/register.html', {'form': form})


# --- Profile View ---
# The @login_required decorator ensures only logged-in users can see this page


@login_required
def profile(request):
    if request.method == 'POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile') 
    else:
        
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'blog/profile.html', context)

# This is a view to display all posts.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted'] 
class PostDetailView(DetailView):
    model = Post

# This view allows a logged-in user to create a new post.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] # Fields the user can fill in

    # sets the author to the currently logged-in user.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# This view allows the author of a post to update it.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/' # Where to redirect after a successful deletion

    # checks if the user trying to delete the post is the author.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False