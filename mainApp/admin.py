from django.contrib import admin
from .models import Genre,Book, Author,Comment, Chapter, Image_chapter, Book_series
# Register your models here.
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Chapter)
admin.site.register(Image_chapter)
admin.site.register(Book_series)
