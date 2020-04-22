from django import forms

class Vhod(forms.Form):
    username = forms.CharField(label='', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

class Regis(forms.Form):
    username = forms.CharField(label='', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(label='', max_length=20)