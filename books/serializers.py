from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Author, Book
from django.db import models

class AuthorModelSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=255)

    class Meta:
        model = Author
        fields = ("id","name")

    def create(self, validated_data):
        """
        根据提供的验证过的数据创建并返回一个新的`Author`实例。
        """
        return Author.objects.create(**validated_data)

class BookModelSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=200)

    # author = serializers.CharField(source="author.id")
    class Meta:
        model = Book
        fields = ("id","title","author")
        # depth =1

        # fields = "__all__"

    # def create(self, validated_data):
    #     """
    #     根据提供的验证过的数据创建并返回一个新的`Author`实例。
    #
    #     """
    #
    #     print("validated_data", validated_data)
    #     authors = validated_data.pop('author')
    #     print("authors", authors)
    #
    #     # book = Book.objects.create(title=validated_data['title'])
    #     book = Book.objects.create(** validated_data)
    #     for author in authors:
    #         author = Author.objects.filter(id=author.id).first()
    #         print(author)
    #         book.author.add(author)
    #         book.save()
    #         # book.author.add(*validated_data["author"])
    #         # book.author.create(**author)
    #     return book


