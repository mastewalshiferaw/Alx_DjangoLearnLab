from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView 
from .models import Library, Books        
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