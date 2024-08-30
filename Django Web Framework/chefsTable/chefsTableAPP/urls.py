from django.urls import path
from . import views

urlpatterns = [
    path('diches/<str:dish>',views.menuitem),
]
