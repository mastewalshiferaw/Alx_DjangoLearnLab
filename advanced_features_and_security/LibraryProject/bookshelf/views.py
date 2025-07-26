from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

from .forms import ExampleForm

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # process data
            pass
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/example.html', {'form': form})




@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
form = SearchForm(request.GET) 