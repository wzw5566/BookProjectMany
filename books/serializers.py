from rest_framework.serializers import ModelSerializer

from rest_framework import serializers
from .models import Product, Category
from django.db import models

class CategorySerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        if 'categories' not in self.fields:
            self.fields['categories'] = CategorySerializer(obj, many=True)
        return super(CategorySerializer, self).to_representation(obj)

    class Meta:
        model = Category
        fields = ("name", 'products', 'categories')

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = ("product_code", "name", "quantity", "price", 'categories')


    def create(self, validated_data):
      category_data = validated_data.pop('categories')
      product = Product.objects.create(**validated_data)
      for category in category_data:
          product.categories.create(**category)
      return product
