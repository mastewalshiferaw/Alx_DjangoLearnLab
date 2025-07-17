author = Author.object.get(name = "Abebe")
books = Book.objects.filter(author=author)

for book in books:
  print(book.title)

