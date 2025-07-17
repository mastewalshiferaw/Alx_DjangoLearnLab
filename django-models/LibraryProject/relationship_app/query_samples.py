author = Author.object.get(name = "Abebe")
books = Book.objects.filter(author=author)

for book in books:
  print(book.title)

library = Library.objects.get(id=1)
books = Book.objects.filter(library=library)

for book in books:
    print(book.title)

library = Library.objects.get(id=1)
librarian = library.librarian  
print(librarian.name)