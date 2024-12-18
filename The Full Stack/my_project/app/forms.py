from django import forms

from .models import UserComents

class CommentForm(forms.ModelForm):
    class Meta:
        model = UserComents
        fields = '__all__'