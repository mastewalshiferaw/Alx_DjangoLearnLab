from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic.detail import DetailView 
from .models import Library, Book, UserProfile 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm    



from django.contrib.auth.decorators import login_required, user_passes_test



def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'



def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user) 
            return redirect('list_books')  
    else:
        form = UserCreationForm()  
    return render(request, 'relationship_app/register.html', {'form': form})



def list_all_books(request):
    
    all_books = Book.objects.all()
    context = {
        'books': all_books

    }

    return render (request, 'relationship_app/list_books.html, context')
   
    all_books = Book.objects.all()
    response_lines = []
    for book in all_books:
        line = f"{book.title} by {book.author.name}"
        response_lines.append(line)
    response_text = "\n".join(response_lines)
    return HttpResponse(response_text, content_type="text/plain")



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

class LibraryDetailView(DetailView):
   
    model = Library

    
    template_name = 'relationship_app/library_detail.html'
    
    context_object_name = 'library'


@login_required
@user_passes_test(is_admin, login_url='/relationships/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/relationships/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/relationships/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')