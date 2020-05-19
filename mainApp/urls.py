"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views
app_name = 'mainApp'
urlpatterns = [
    path('', views.home, name="Главная страница"),
    path('about/', views.about, name="О нас"),
    path('genres/', views.genre, name="Жанры"),
    path('genres/<str:name_genre>_<int:genre_id>/', views.genre_detail, name="genre_detail"),
    path('<str:name_book>_<int:book_id>/', views.book_detail, name="book_detail"),
    path('<str:name_book>_<int:book_id>/leave_comment', views.leave_comment, name="leave_comment"),
    path('search/', views.search_books, name="search_books")
]
