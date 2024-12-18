from django.shortcuts import render
from app.forms import CommentForm
from .models import UserComents
from django.http import JsonResponse

def form_view(request):
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uc = UserComents(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment'],
            )
            uc.save()
            
    return render(request, 'blog.html', {'form': form})