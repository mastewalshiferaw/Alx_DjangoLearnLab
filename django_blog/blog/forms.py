from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment

# Our custom form inherits from Django's UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # We add an email field, and make it required
    email = forms.EmailField(required=True, help_text='Required. Please provide a valid email address.')

    class Meta(UserCreationForm.Meta):
        # We start with the default model and fields
        model = User
        # new 'email' field to the list of fields to display
        fields = UserCreationForm.Meta.fields + ('email',)
    
    class UserUpdateForm(forms.ModelForm):
        email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    # We add an email field to ensure it's included in the form.
    email = forms.EmailField()

    class Meta:
        # This form is built from the User model.
        model = User
        # These are the fields the user will be able to edit on their profile.
        fields = ['username', 'email']
        
class CommentForm(forms.ModelForm):
    class Meta: #it is where you connect your form to your model and configure it is behaviour 
        model = Comment

        fields = ['content']

