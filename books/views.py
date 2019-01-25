from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer

# Create your views here.
class JSONResponse(HttpResponse):
  """
  An HttpResponse that renders its content into JSON.
  """

  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def createProduct(request):
  """
  创建产品
  :param request:
  :return:
  """