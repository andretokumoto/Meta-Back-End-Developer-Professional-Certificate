from django.shortcuts import render
from django.db import IntegrityError
from django.http import JsonResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = list(Book.objects.all().values())
        return JsonResponse({'books': books})

    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        try:
            book = Book(title=title, author=author, price=price)
            book.save()
            return JsonResponse(model_to_dict(book), status=201)
        except IntegrityError:
            return JsonResponse({'error': 'true', 'message': 'required field missing'}, status=400)
