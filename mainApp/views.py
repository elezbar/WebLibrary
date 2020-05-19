from django.shortcuts import render
from .models import Book,Chapter,Book_series,Genre
from  django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q

# Create your views here.
import parser
def home (request):
    book = Book.objects.order_by('-publication_date')
    return render(request, 'mainApp/homePage.html',{'book': book})

def about(request):
    return render(request, 'mainApp/about.html')

def book_detail(request, name_book , book_id ):
    try:
        b = Book.objects.get(id = book_id)
    except:
        raise Http404("Книга не найдена!")
    if (name_book != b.name_book):
        raise Http404("Книга не найдена!")
    chapters = Chapter.objects.filter(book = b.id)
    chapters = chapters.order_by("name_chapter")
    another_book = Book.objects.filter(series = b.series)
    another_book = another_book.exclude(id = b.id)
    series = Book_series.objects.get(name_series = b.series)
    comment = b.comment_set.order_by('-id')[:10]
    return render(request, 'mainApp/book.html', {'book':b, 'chapter':chapters, 'another_book_in_series':another_book, 'series':series , 'comment':comment})

def genre(request):
    genres = Genre.objects.all()
    return render(request, 'mainApp/genres.html', {'genres': genres})

def genre_detail(request, name_genre, genre_id):
    try:
        g = Genre.objects.get(id = genre_id)
    except:
        raise Http404("Жанр не найден!")
    if (name_genre != g.name_genre):
        raise Http404("Жанр не найден!")
    book = Book.objects.filter(genres_book__id = genre_id )
    return render(request, 'mainApp/homePage.html', {'book':book})

def leave_comment(request, name_book, book_id):
    try:
        b = Book.objects.get(id = book_id)
    except:
        raise Http404("Книга не найдена!")
    b.comment_set.create(author_name = request.POST.get('name', False), comment_text = request.POST.get('text', False))
    return HttpResponseRedirect(reverse('mainApp:book_detail',args = (b.name_book, b.id,)))

def search_books(request):
    try:
        b = Book.objects.filter(Q(name_book__icontains = request.POST.get('search',False)) | Q(authors__name_author__icontains = request.POST.get('search',False)))
    except:
        raise Http404("Книг не найдено!")
    return render(request, 'mainApp/homePage.html', {'book':b})
