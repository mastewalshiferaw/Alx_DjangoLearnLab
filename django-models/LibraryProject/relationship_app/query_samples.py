from relationship_app.models import Author, Book, Library, Librarian


author_name = "Abebe"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

for book in books:
  print(book.title)

library_name = "Central Library"
library = Library.objects.get(name=library_name) 
books_in_library = library.books.all()

librarian = Librarian.objects.get(library=library)

print(f"Librarian: {librarian.name}")