from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language             #Import Models

# Register your models here.
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(Book)

#Inline classes must be defined before used in other classes...duh
class BooksInline(admin.TabularInline):
    model = Book


#Define admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

#Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# class BooksInline(admin.TabularInline):
#     model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# admin.site.register(BookAdmin)                    #Register BookAdmin

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    list_display = ('book', 'status', 'due_back', 'id')

    fieldsets = (
        (None,
            {
                'fields': ('book', 'imprint', 'id')
            }
        ),
        ('Availability',
            {
                'fields': ('status', 'due_back')
            }
        ),
    )
