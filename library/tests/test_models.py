from django.test import TestCase
from library.models import Author
from library.models import Genre
from library.models import Language
from library.models import Book
from library.models import BookInstance
from datetime import date

class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(name='tester_hoyeon')
    
    def test_name_label(self):
        author = Author.objects.get(id=1)
        name_label = author._meta.get_field('name')
        self.assertEquals(name_label.name, 'name')
    
    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        birth_label = author._meta.get_field('date_of_birth')
        self.assertEquals(birth_label.name, 'date_of_birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        death_label = author._meta.get_field('date_of_death')
        self.assertEquals(death_label.name, 'date_of_death')
    
    def test_name_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name(self):
        author = Author.objects.get(id=1)
        object_name = author.name
        self.assertEquals(str(author), object_name)

    def test_absolute_url(self):
        # before test this function. first set urls config
        pass


class GenreModelTest(TestCase):

    def setUp(self):
        Genre.objects.create(name="Test genre")
    
    def test_name_label(self):
        genre = Genre.objects.get(id=1)
        name_label = genre._meta.get_field('name')
        self.assertEquals(name_label.name, 'name')

    def test_object_name(self):
        genre = Genre.objects.get(id=1)
        object_name = genre.name
        self.assertEquals(str(genre), object_name)

    def test_name_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)


class LanguageModelTest(TestCase):

    def setUp(self):
        Language.objects.create(name="Test genre")
    
    def test_name_label(self):
        language = Language.objects.get(id=1)
        name_label = language._meta.get_field('name')
        self.assertEquals(name_label.name, 'name')

    def test_object_name(self):
        language = Language.objects.get(id=1)
        object_name = language.name
        self.assertEquals(str(language), object_name)    
    
    def test_name_length(self):
        language = Language.objects.get(id=1)
        max_length = language._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author_ = Author.objects.create(
            name="Tester",
            date_of_birth=date.today(),
            date_of_death=date.today()
        )
        Genre_ = Genre.objects.create(
            name="Test genre"
        )
        Language_ = Language.objects.create(
            name="ENG"
        )
        instance = Book.objects.create(
            title="Test title",
            author=Author_,
            isbn="12312412412",
            language=Language_
        )
        instance.genre.set(Genre.objects.filter(name="Test genre"))

    def test_title_label(self):
        book = Book.objects.get(id=1)
        title_label = book._meta.get_field('title')
        self.assertEquals(title_label.name, 'title')

    def test_created_properly(self):
        self.assertEquals(
            1, 
            len(Book.objects.filter(
                author__in=Author.objects.filter(name="Tester")
                )
            )
        )