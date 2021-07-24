from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


def index(request):
    pass


class BookListView(generic.ListView):
    model = Book
    template_name = "library/book_list.html"
    paginate_by = 10


class AuthorListView(generic.ListView):
    model = Author
    template_name = "library/author_list.html"
    paginate_by = 10