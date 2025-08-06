
from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model instances. It includes a custom validation
    rule to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        # All fields from the Book model will be included.
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Checks that the publication year is not a future year."""
        if value > datetime.date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model instances. It demonstrates how to handle
    nested relationships by including a serialized list of the author's books.
    """
    # This line creates the nested serialization.
    # 'books' matches the `related_name` in the Book model's ForeignKey.
  
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']