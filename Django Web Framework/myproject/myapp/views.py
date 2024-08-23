from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome !!!!")

def hello(request):
    return HttpResponse("Hello World !!!!")

def return_form(request):
    text = """<h1 style="color : #F4CE14;"> Ta Formatado </h1>"""
    return HttpResponse(text)