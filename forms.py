from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
class CreateUserForm(UserCreationForm):
    Username=forms.CharField()
    email=forms.EmailField()
    password1=forms.PasswordInput()
    password2=forms.PasswordInput()
    #phonenumber=forms.CharField()
    
    
    class Meta:
        model=User
        fields=['Username', 'email','password1','password2']

