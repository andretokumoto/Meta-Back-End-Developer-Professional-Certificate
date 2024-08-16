from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Heloo to my APP')