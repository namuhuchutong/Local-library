from django.contrib import admin
from .models import Author, Genre, Book, Language, BookInstance

admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_of_birth',
        'date_of_death',
    )
    fields = [
        'name',
        ('date_of_birth', 'date_of_death'),
    ]
    inlines = [BookInline]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
    )
    inlines = [BookInstanceInline]

admin.site.register(Book, BookAdmin)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'status',
        'borrower',
        'due_back',
        'id',
    )
    list_filter = (
        'status',
        'due_back',
    )

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Advanced options', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )