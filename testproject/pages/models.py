from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Автори'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=25)
    publication_date = models.DateField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )
    rating = models.IntegerField()

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['publication_date']
        constraints = [
            models.UniqueConstraint(fields=['publication_date'], name='unique_publication_date')
        ]

    def __str__(self):
        return self.title


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book,  through='PublisherCompany')

    class Meta:
        verbose_name_plural = 'Видавництва'

    def __str__(self):
        return self.name


class PublisherCompany(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Книги Видавництв'


class Category(models.Model):
    name = models.CharField(max_length=50, unique_for_month='created_date')
    created_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name








