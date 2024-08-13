from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book, Category, Publisher, Author


def get_sidebar_authors():
    return Author.objects.all()


def home_view(request):
    return render(request, 'home_page.html', {'all_authors': get_sidebar_authors()})


def author_list(request):
    author = Author.objects.filter(age__lte=35)
    return render(request, 'authors_list.html', {'Authors': author, 'all_authors': get_sidebar_authors()})


def author_books_view(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'author_books.html', {'Author': author, 'Books': books, 'all_authors': get_sidebar_authors()})


def books_view(request):
    books = Book.objects.filter(rating__gte=1)
    return render(request, "book_list.html", {'Books': books, 'all_authors': get_sidebar_authors()})


def category_view(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {'Categories': categories, 'all_authors': get_sidebar_authors()})


def publisher_view(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'Publishers': publishers, 'all_authors': get_sidebar_authors()})
