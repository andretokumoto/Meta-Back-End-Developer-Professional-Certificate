from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.sobre, name="sobre"),
    path('menu', views.menu, name="menu"),
    path('reserva', views.reservar, name="reserva"),
]
