from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first(request):
    return HttpResponse('<h1>Iam in bangalore</h1>')

def second(request):
    return HttpResponse('<h1>Hiiii!!!helloo world</h1>')