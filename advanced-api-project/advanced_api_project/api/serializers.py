from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    
    #Serializes all fields of the Book model.
    Includes custom validation to ensure publication_year is not in the future.
    
    
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'  # Includes: id, title, publication_year, author


class AuthorSerializer(serializers.ModelSerializer):
    
    #Serializes the Author model with the name field and a nested list of books.
    
  
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']  
  