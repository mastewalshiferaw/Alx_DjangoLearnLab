from django.db import models

# Create your models here


from django.db import models

class Author(models.Model):
    """
    This model represents an Author.
    It stores the author's name and is linked to the books they have written.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    This model represents a Book.
    It includes the book's title, publication year, and a
    foreign key relationship to its Author. The `related_name='books'`
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        