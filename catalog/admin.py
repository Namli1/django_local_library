from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from catalog.models import Author, Genre, Book, BookInstance, Language

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BorrowedBooksInline(admin.TabularInline):
    model = BookInstance


#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language', )
    inlines = [BookInstanceInline]
# admin.site.register(Author)
class BookInline(admin.TabularInline):
    model = Book
    extra = 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id',)
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
admin.site.register(Language)

class UserAdmin(UserAdmin):
    inlines = [BookInstanceInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)