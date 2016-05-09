from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class LoginForm(UserCreationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = { 'password' : forms.PasswordInput()}

    def save(self,commit = True):
        user = authenticate(username=username, password=password)

        return user

