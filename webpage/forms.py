from django import forms
from .models import Sms1

class Sms1Form(forms.ModelForm):
    sender = forms.BooleanField(default=False)
    main = forms.BooleanField(default=True)
    date = forms.BooleanField(default=False)
    link = forms.BooleanField(default=True)
    class Meta:
       model = Sms1
       #field = ['sender', 'main', 'date', 'link']