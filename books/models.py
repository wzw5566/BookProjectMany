from django.db import models
from django.contrib.contenttypes.models import ContentType


class Author(models.Model):
  name = models.CharField(max_length=255, unique=True)


class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ManyToManyField(Author, related_name="author_related")

