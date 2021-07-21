from django.test import TestCase
from library.models import Author

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