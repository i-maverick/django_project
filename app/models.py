from django.db import models
import json


class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    publication_year = models.IntegerField(null=True)
    isbn = models.CharField(max_length=17, blank=True, verbose_name='ISBN-13')

    def __str__(self):
        return self.title

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)
