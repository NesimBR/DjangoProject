from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    catid = forms.IntegerField()


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name :')
    email = forms.EmailField(max_length=200, label='Email :')
    first_name = forms.CharField(max_length=100,help_text='First Name', label='First Name :')
    last_name = forms.CharField(max_length=100,help_text='Last Name', label='Last Name :')

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2'}





