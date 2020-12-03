from base.settings import TEMPLATES
from django.shortcuts import render
from django.core import serializers
from django.http.response import HttpResponse
from .models import Post
import json

# Create your views here.


def index(request):
    template = 'posts/index.html'
    resultados = Post.objects.all()
    context = {'resultados': resultados}
    return render(request, template, context)


def base_layout(request):
    template = 'posts/base.html'
    return render(request, template)

def getdata(request):
    resultados = Post.objects.all()
    jsondata = serializers.serialize('json', resultados)
    return HttpResponse(jsondata)