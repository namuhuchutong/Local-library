from django.urls import path

from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name="books"),
    path('authors/', views.AuthorListView.as_view(), name="authors"),    
]