from django.db import models

from django.conf import settings

class UserProfile(models.Model):
    
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

    def __str__(self):
        
        return self.user.username

    
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        
        return f'{self.user.username} - {self.role}'









class Author(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name
  
class Book(models.Model):
  title = models.CharField(max_length=150)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
class Library(models.Model):
  name = models.CharField(max_length=200)
  books = models.ManyToManyField(Book)
class Librarian(models.Model):
  name= models.CharField(max_length=200)
  library = models.OneToOneField(Library, on_delete=models.CASCADE)


class Meta:
   permissions = (
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),("can_delete_book", "Can delete book")
        )