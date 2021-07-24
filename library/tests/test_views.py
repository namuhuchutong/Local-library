from django.test import TestCase
from django.urls import reverse

from library.models import Author, Book, Genre, Language
import uuid

class AuthorListViewTest(TestCase):
    
    def setUp(self):
        num_of_authors = 13
        for author_id in range(num_of_authors):
            Author.objects.create(name="Tester {0}".format(author_id))
    
    def test_view_url_response(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_correct_tempaltes(self):
        response = self.client.get(reverse('authors'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/author_list.html')

    def test_view_pagination(self):
        response = self.client.get(reverse('authors'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 10)


class BookListViewTest(TestCase):
    
    def setUp(self):
        num_of_books = 13
        Genre_ = Genre.objects.create(name="Test genre")
        Language_ = Language.objects.create(name="ENG")
        
        for book_id in range(num_of_books):
            Author_ = Author.objects.create(name="tester {0}".format(book_id))
            instance = Book.objects.create(
                title="Test book {0}".format(book_id),
                author=Author_,
                isbn=uuid.uuid4(),
                language=Language_
            )
            instance.genre.set(Genre.objects.filter(name="Test genre"))

    def test_view_url_response(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
    
    def test_view_correct_tempaltes(self):
        response = self.client.get(reverse('books'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/book_list.html')

    def test_view_pagination(self):
        response = self.client.get(reverse('books'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), 10)