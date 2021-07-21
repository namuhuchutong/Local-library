from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
import uuid



class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Input a book genre"
    )

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Input a book's language"
    )

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Input a author's name"
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    date_of_death = models.DateField(
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(
        max_length=200
    )
    author = models.ForeignKey(
        Author, 
        on_delete=models.SET_NULL, 
        null=True
    )
    isbn = models.CharField(
        max_length=200,
        unique=True,
    )
    genre = models.ManyToManyField(
        Genre
    )
    language = models.ForeignKey(
        Language, 
        on_delete=models.SET_NULL, 
        null=True
    )

    class Meta:
        ordering = ['title', 'author']

    def show_genre(self):
        return ', '.join(
            [genre.name for genre in self.genre.all()]
        )

    def get_absoulte_url(self):
        return reverse(
            'book-detail', 
            args=[str(self.id)]
        )
    
    def __str__(self):
        return self.title

class BookInstance(models.Model):

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='d'
    )
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    imprint = models.CharField(
        max_length=100
    )
    due_back = models.DateField(
        null=True,
        blank=True
    )
    borrower = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    
    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

