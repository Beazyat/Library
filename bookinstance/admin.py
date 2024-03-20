from django.contrib import admin
from .models import *
# Register your models here.


class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "author")
    inlines = [BookInstanceInline]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")

    
@admin.register(BookInstance)
class InstanceAdmin(admin.ModelAdmin):  
    list_display = ("book", "status", "borrower", 'due_back', 'id')
    list_filter = ('status', 'due_back')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)

    
@admin.register(Book_Genre)
class Set_genreAdmin(admin.ModelAdmin):    
    list_display = ("book", "genre")


