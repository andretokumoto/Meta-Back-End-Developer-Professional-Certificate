
from . import views
from django.urls import path,include

#menu_itens
urlpatterns = [
    #path('ratings/', views.RatingsView.as_view(), name='ratings'),
    path('menu_item/',views.menu_itens),
]
