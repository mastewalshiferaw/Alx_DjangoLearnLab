from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm 

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