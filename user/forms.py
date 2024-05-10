from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    Full_name=forms.CharField()
    Phone_number=forms.IntegerField()
    class Meta:
        model = User
        fields = ['Full_name', 'username', 'email', 'Phone_number', 'password1', 'password2']