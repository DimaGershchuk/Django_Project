from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Автори'


class Book(models.Model):
    title = models.CharField(max_length=25)
    publication_date = models.DateField()
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        unique=True
    )
    rating = models.IntegerField()

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['publication_date']
        constraints = [
            models.UniqueConstraint(fields=['publication_date'], name='unique_publication_date')
        ]


class Publisher(models.Model):

    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book,  through='PublisherCompany')

    class Meta:
        verbose_name_plural = 'Видавництва'


class PublisherCompany(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Книги Видавництв'


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Категорії'
        constraints = [
            models.UniqueConstraint(fields=['name', 'created_date'], name='unique_category_name_per_month')
        ]








