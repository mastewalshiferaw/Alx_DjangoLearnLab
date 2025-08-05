from django.db import models
from django.contrib.auth.models import AbstractUser

class Author(models.Model):
  #Author model stores individual authors.

  name = models.CharField(max_length=200)

class Book(models.Model):
    #Book model represents books written by authors.
    #Each book is linked to a single author using a ForeignKey.
    #publication_year is used to track the year the book was published.

  title = models.CharField(max_length=100)
  puublication_year = models.IntegerField(null=True, blank=True)
  author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name='books')

  def __str__(self):
    return self.title 

