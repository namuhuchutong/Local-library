from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            "num_books":num_books,
            "num_instances":num_instances,
            "num_instances_available:":num_instances_available,
            "num_authors":num_authors,
        }
    )

class BookListView(generic.ListView):
    model = Book
    template_name = "library/book_list.html"
    paginate_by = 10


class AuthorListView(generic.ListView):
    model = Author
    template_name = "library/author_list.html"
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "library/book_detail.html"


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "library/author_detail.html"