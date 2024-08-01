from django.contrib import admin
from .models import Author, Book, Publisher, PublisherCompany, Category

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(PublisherCompany)
admin.site.register(Category)


