from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from books.models import Book,Author
from books.serializers import BookModelSerializer,AuthorModelSerializer
from rest_framework import viewsets

class BookList(APIView):
  def get(self, request):
    books = Book.objects.all()
    serializer = BookModelSerializer(books, many=True)
    return Response(serializer.data)

  def post(self, request, *args, **kwargs):
    data = request.data
    serializer = BookModelSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorList(APIView):
  def get(self, request):
    authors = Author.objects.all()
    serializer = AuthorModelSerializer(authors, many=True)
    return Response(serializer.data)

  def post(self, request):
    data = request.data
    print(data)
    serializer = AuthorModelSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

class AhthorViewSet(viewsets.ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorModelSerializer