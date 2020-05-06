from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import TextInput, FileInput, EmailInput

from home.models import UserProfile


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username' : TextInput(attrs={'class': 'form-control form-group row col-sm-12','placeholder': 'username'}),
            'email' : EmailInput(attrs={'class': 'form-control form-group row col-sm-12','placeholder': 'email'}),
            'first_name' : TextInput(attrs={'class': 'form-control form-group row col-sm-12','placeholder': 'first_name'}),
            'last_name' : TextInput(attrs={'class': 'form-control form-group row row col-sm-12','placeholder': 'last_name'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ( 'phone', 'country', 'university', 'department', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'form-control form-group row col-sm-12', 'placeholder': 'phone'}),
            'country': TextInput(attrs={'class': 'form-control form-group row col-sm-12', 'placeholder': 'country'}),
            'university': TextInput(attrs={'class': 'form-control form-group row col-sm-12', 'placeholder': 'university'}),
            'department': TextInput(attrs={'class': 'form-control form-group row col-sm-12', 'placeholder': 'department'}),
            'image': FileInput(attrs={'class': 'form-group row col-sm-10 custom-file  row col-sm-12', 'id': 'user_image','type': 'file'}),
        }