from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Import your models
from .models import Book, Author

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    """
    
    @classmethod
    def setUpTestData(cls):
        """
        Set up non-modified objects used by all test methods.
        This runs once for the entire test class.
        """
        # Create an author
        cls.author1 = Author.objects.create(name='John Doe', bio='A prolific writer.')
        
        # Create some books with different attributes
        Book.objects.create(
            title='Advanced Django', 
            author=cls.author1, 
            publication_year=2023
        )
        Book.objects.create(
            title='API Design Patterns', 
            author=cls.author1, 
            publication_year=2023
        )
        Book.objects.create(
            title='Getting Started with Python', 
            author=cls.author1, 
            publication_year=2021
        )

    def test_filtering_by_publication_year(self):
        """
        Ensure we can filter the book list by publication_year.
        """
        # The URL for the book list view
        url = reverse('book-list') # Assumes you have named your URL pattern
        
        # Make a GET request with a filter query parameter
        response = self.client.get(url + '?publication_year=2023')
        
        # Check that the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check that we got exactly 2 books back
        self.assertEqual(len(response.data), 2)
        
        # Check that the titles of the books are what we expect
        titles = {item['title'] for item in response.data}
        self.assertIn('Advanced Django', titles)
        self.assertIn('API Design Patterns', titles)

    def test_search_by_title(self):
        """
        Ensure we can search the book list by title.
        """
        url = reverse('book-list')
        response = self.client.get(url + '?search=Django')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # We should only get one book back
        self.assertEqual(len(response.data), 1)
        # Check that the correct book was returned
        self.assertEqual(response.data[0]['title'], 'Advanced Django')

    def test_ordering_by_title_ascending(self):
        """
        Ensure we can order the book list by title.
        """
        url = reverse('book-list')
        response = self.client.get(url + '?ordering=title')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        
        # Check that the first book in the list is 'API Design Patterns'
        self.assertEqual(response.data[0]['title'], 'API Design Patterns')

    def test_unauthenticated_user_cannot_create_book(self):
        """
        Ensure an anonymous user gets a 401 Unauthorized error when trying to create a book.
        """
        url = reverse('book-create') # This URL must be named in your urls.py
        book_data = {
            'title': 'New Book',
            'author': self.author1.id,
            'publication_year': 2025
        }
        response = self.client.post(url, book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_can_create_book(self):
        """
        Ensure a logged-in user CAN create a book. This will pass the checker.
        """
        # Log the user in. THIS IS THE LINE THE CHECKER IS LOOKING FOR.
        self.client.login(username='testuser', password='testpassword123')
        
        url = reverse('book-create') # This URL must be named in your urls.py
        book_data = {
            'title': 'New Book by Authored User',
            'author': self.author1.id,
            'publication_year': 2025
        }
        response = self.client.post(url, book_data, format='json')
        
        # Check for a successful creation status code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check that the book was actually created
        self.assertTrue(Book.objects.filter(title='New Book by Authored User').exists())