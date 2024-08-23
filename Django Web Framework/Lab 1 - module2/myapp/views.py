from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    text = """<h1> Welcome to Little Lemon! </h1> """
    return HttpResponse(text)
