from django.urls import path
from . import views

'''
urlpatterns = [
    path('books/',views.books)
]
'''
urlpatterns = [
	path('orders', views.Orders.listOrders)
]