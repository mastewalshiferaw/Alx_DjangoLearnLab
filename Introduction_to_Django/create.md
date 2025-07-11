after opening the Django shell with "py manage.py shell"
I was prompt to the shell, on the shell I created a book instance by giving a command bellow:

from bookshelf.models import Book
book = Book(title=1984, author="George Orwell", publication_year = 1949)
and finally I saved it usng: book.save()
No change in the output it just preceded
