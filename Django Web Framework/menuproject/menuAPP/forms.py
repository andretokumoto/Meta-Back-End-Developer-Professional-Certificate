from django import forms
from .models import Logger

'''
SHIFTS = [
    ('1','Morning'),
    ('2','Afternoon'),
]

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    first_last = forms.CharField(max_length=200)
   # shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField()
    '''
    
class LogForm(forms.ModelForm):
    class meta:
        model = Logger
        fields ='__all__'