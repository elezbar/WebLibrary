from django.db import models
from django.utils import timezone
# Create your models here.
class Book_series(models.Model):
   name_series = models.CharField('Название серии', max_length = 50)
   image_series = models.ImageField(upload_to = 'static', blank=True)
   def __str__(self):
       return self.name_series

class Genre(models.Model):
    name_genre = models.CharField('Жанр', max_length = 50)
    def __str__(self):
        return self.name_genre

class Author(models.Model):
    name_author = models.CharField('Имя автора', max_length = 50)
    biographi = models.CharField('Биография', max_length = 500)
    def __str__(self):
        return self.name_author

class Book(models.Model):
    """docstring for Book."""

    series = models.ForeignKey(Book_series, on_delete = models.CASCADE, null=True)
    name_book = models.CharField('Название книги', max_length = 50)
    annotation = models.CharField('Аннотация к книге', max_length = 300, blank=True)
    publication_date = models.DateTimeField('Дата публицации')
    genres_book = models.ManyToManyField(Genre, verbose_name="Жанры книги")
    authors = models.ManyToManyField(Author, verbose_name="Авторы")
    image_book = models.ImageField(upload_to = 'static', blank=True)
    def __str__(self):
        return self.name_book


class Comment(models.Model):
    """docstring for comment."""
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    author_name = models.CharField('Псевдоним', max_length = 20)
    comment_text = models.CharField('Текст комментария', max_length = 300)

    def __str__(self):
        return self.author_name

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    name_chapter = models.CharField('Название главы', max_length = 30)
    chapter_text = models.TextField('Содержание главы')

    def __str__(self):
        d = Book.objects.get(name_book = self.book)
        return   d.name_book+' '+self.name_chapter

class Image_chapter(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete = models.CASCADE)
    Image_chapter = models.ImageField(upload_to = 'static')
    def __str__(self):
        return self.image_chapter_directory

class Book_raiting(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
