from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
def home(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html', {})