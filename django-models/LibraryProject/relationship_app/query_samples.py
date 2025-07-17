from relationship_app.models import Library, Book, Librarian


author = Author.object.get(name = "Abebe")
books = Book.objects.filter(author=author)

for book in books:
  print(book.title)

library_name = "Central Library"

library = Library.objects.get(name = "Library_name")


for book in books:
    print(book.title)

library = Library.objects.get(id=1)
librarian = library.librarian  
print(librarian.name)