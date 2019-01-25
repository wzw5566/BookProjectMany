from django.db import models
from django.contrib.contenttypes.models import ContentType


class Category(models.Model):
  name = models.CharField(max_length=255)
  categoriesId = models.ForeignKey('self', related_name='categories', on_delete=models.CASCADE, blank=True, null=True)


class Product(models.Model):
  product_code = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  price = models.IntegerField()
  quantity = models.IntegerField()
  categories = models.ManyToManyField(Category, related_name='products')

