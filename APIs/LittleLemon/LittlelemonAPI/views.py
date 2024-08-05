from django.shortcuts import get_object_or_404
#from django.http import JsonResponse
#from django.views import View
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Menuitem
from .serializers import MenuItemSerializar

'''
class RatingsView(View):
    def get(self, request):
        return JsonResponse({'message': 'Ratings view'})
'''

@api_view(['GET','POST'])
def menu_itens(request):
    if request.method == 'GET':
        itens = Menuitem.objects.all()
        serialized_item = MenuItemSerializar(itens, many = True)
        return Response(serialized_item.data) 
    if request.method == 'POST':
        serialized_item = MenuItemSerializar(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view()
def single_item(request, id):
    item = get_object_or_404(Menuitem, pk=id)
    serialized_item = MenuItemSerializar(item)
    return Response(serialized_item.data)