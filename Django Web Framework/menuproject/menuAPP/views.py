from django.shortcuts import render
from django.http import HttpResponse
from menuAPP.forms import LogForm
from .models import Menu

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

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dic = {'menu': newmenu}
    return render(request, 'menu.html', newmenu_dic)
    