from django.test import TestCase

# Create your tests here.

from rest_framework.test import APIClient
from .models import Book
import datetime

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            isbn='1234567890123',
            published_date=datetime.date.today()
        )

    def test_list_books(self):
        resp = self.client.get('/api/books/')
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json(), list)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "isbn": "3210987654321",
            "published_date": "2023-01-01"
        }
        resp = self.client.post('/api/books/', data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()['title'], 'New Book')

    def test_update_book(self):
        resp = self.client.patch(f'/api/books/{self.book.id}/', {'title': 'Updated'}, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['title'], 'Updated')
