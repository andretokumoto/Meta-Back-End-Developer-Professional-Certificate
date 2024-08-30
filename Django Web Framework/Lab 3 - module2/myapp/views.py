from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    response = HttpResponse('Welcome to Little Lemon!')
    return response

def sobre(request):

    response = HttpResponse('Sobre nós')
    return response

def menu(request):

    response = HttpResponse('Menu')
    return response

def reservar(request):

    response = HttpResponse('Fazer uma reserva')
    return response
