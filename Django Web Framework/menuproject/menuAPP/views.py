from django.shortcuts import render
from django.http import HttpResponse
from menuAPP.forms import LogForm

def form_view(request):
    form = LogForm()
    
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {"Form":form}
    return render(request, 'menuAPP/home.html', context)


def menu(request):
    menuitem = {'name':'Burrito'}
    return render(request, 'menu.html', menuitem)