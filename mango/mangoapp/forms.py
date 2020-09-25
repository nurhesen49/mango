from django import forms
from django.contrib.auth.models import User
from .models import UserModel


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields=['username', 'password', 'email']

class UserExtra(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['potfolio_site']
