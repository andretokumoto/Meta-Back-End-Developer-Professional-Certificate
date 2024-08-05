#from django.shortcuts import render
#from django.http import JsonResponse
#from django.views import View
from rest_framework.response import Response
#from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from .models import Menuitem
from .serializers import MenuItemSerializar

'''
class RatingsView(View):
    def get(self, request):
        return JsonResponse({'message': 'Ratings view'})
'''

@api_view()
def menu_itens(request):
    itens = Menuitem.objects.all()
    serialized_item = MenuItemSerializar(itens, many = True)
    return Response(serialized_item.data) 