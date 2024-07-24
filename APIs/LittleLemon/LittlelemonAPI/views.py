from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

class RatingsView(View):
    def get(self, request):
        return JsonResponse({'message': 'Ratings view'})
