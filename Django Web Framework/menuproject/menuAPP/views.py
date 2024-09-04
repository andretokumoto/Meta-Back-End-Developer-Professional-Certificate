from django.shortcuts import render
from django.http import HttpResponse
from menuAPP.forms import InputForm

def form_view(request):
    form = InputForm()
    context = {"Form":form}
    return render(request, 'menuAPP/home.html', context)


