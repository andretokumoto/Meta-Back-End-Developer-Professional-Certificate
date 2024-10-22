from django import forms
from .models import Reserva

class BookingForm(forms.ModelForm):
    class meta:
        model = Reserva
        fields = '__all__'