
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('books/', views.books_view, name='books'),
    path('authors/', views.author_list, name='authors'),
    path('author/<int:author_id>/', views.author_books_view, name='author_books'),
    path('categories/', views.category_view, name='categories'),
    path('publishers/', views.publisher_view, name='publishers')

]