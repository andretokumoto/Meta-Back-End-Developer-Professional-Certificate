from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.form_view),
    path('menu/',views.menu),
    path('menu_card/',views.menu_by_id),
]
