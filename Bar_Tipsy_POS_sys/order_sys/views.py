from django.shortcuts import render
from django.views import generic
from django.http import Http404
# Create your views here.

def index(request):
    return render(request, 'index.html')