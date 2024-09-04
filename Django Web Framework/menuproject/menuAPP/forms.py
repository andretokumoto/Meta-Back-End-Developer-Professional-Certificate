from django import forms

FAVORITE_DISH = [
    ('italian','Italian'),
    ('brasilian','Brasilian'),
]

class DemoForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    favorite_dish = forms.ChoiceField(choices=FAVORITE_DISH)