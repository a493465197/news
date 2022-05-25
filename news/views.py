import imp
from django.shortcuts import render
from pathlib import Path
import os

# Create your views here.

from django.http import HttpResponse
# from ..newsWeb import model
BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    # ret = model.newsina.objects().count()
    return HttpResponse('ret')
