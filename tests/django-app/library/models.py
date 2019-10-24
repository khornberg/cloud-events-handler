from django.db import models


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()


class Book(models.Model):
    name = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    published = models.DateField()


class PaperSource(models.Model):
    company = models.TextField()
