from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # إنشاء مستخدمين
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.admin_user = User.objects.create_superuser(username="admin", password="admin123")

        # إنشاء مؤلف وكتب
        self.author = Author.objects.create(name="Author One")
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author)

        # إنشاء client وتسجيل دخول المستخدم العادي
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')  # ✅ هذا المطلوب

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        url = reverse('book-create')
        data = {"title": "Book Three", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        self.client.logout()  # تسجيل خروج المستخدم
        url = reverse('book-create')
        data = {"title": "Book Three", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # DRF يستخدم 403 لمستخدمي session

    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {"title": "Updated Book One", "publication_year": 2020, "author": self.author.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_publication_year(self):
        url = reverse('book-list') + '?publication_year=2020'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        url = reverse('book-list') + '?search=Book Two'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))
