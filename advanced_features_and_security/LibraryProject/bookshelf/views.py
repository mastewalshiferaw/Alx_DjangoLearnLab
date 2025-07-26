from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import forms


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['q']
        results = MyModel.objects.filter(name__icontains=query)



@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
