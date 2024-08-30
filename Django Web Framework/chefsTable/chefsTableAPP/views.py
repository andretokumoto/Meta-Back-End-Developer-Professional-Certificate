from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Heloo to my APP')

def menuitem(request,dish):
    items = {
        'pasta':'is pasta',
        'cook':'good cook',
        'meat':'delicious one'
    }
    
    description = items[dish]
    
    return HttpResponse(f"<h2> {dish} </h2>"+ description)