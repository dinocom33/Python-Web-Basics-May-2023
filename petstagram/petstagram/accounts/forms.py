from enum import unique

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    # username = forms.CharField(min_length=4, max_length=30)
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    email = forms.CharField(label='email', max_length=100)
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'confirm password'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last name'}),
        }
        label = {
            'username': 'Username',
            'password1': 'Password',
            'password2': 'Confirm password',
            'email': 'Email',
            'first_name': 'First Name',
            'last_name': 'Last name',
        }
