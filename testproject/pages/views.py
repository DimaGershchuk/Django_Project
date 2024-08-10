from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Book, Category, Publisher, Author


def home_view(request):
    return render(request, 'home_page.html')


def author_list(request):
    author = Author.objects.filter(age__lte=35)
    return render(request, 'authors_list.html', {'Authors': author})


def author_books_view(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'author_books.html', {'Author': author, 'Books': books})


def books_view(request):
    books = Book.objects.filter(rating__gte=1)
    return render(request, "book_list.html", {'Books': books})


def category_view(request):
    categories = Category.objects.all()
    return render(request, "category_list.html", {'Categories': categories})


def publisher_view(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'Publishers': publishers})
