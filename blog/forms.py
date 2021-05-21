from django import forms
from django.forms import ModelForm, fields
from blog.models import contact

class StudentRegistration(forms.Form):
    name= forms.CharField()
    email=forms.EmailField()

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields=['name','email','phone']

