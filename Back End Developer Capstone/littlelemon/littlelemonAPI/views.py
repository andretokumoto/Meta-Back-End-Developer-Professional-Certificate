from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .serializers import MenuSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html', {})