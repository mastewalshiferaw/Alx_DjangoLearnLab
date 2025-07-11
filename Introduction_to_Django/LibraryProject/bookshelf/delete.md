>>>from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four") # (first I identified what I want to delete by the given updated title name)
>>>book.delete() #This delete the created book
(1, {'bookshelf.Book': 1})
and finally to verify deletion I run the command
>>> Book.objects.all()
<QuerySet []>
clearly showing that the book instance I created is deleted successfully