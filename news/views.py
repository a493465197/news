from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from ..newsWeb import model


def index(request):
    # ret = model.newsina.objects().count()
    return HttpResponse('ret')
