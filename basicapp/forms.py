from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class LoginUser(AuthenticationForm):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        max_length=20, widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["username", "password"]


class RegisterUser(UserCreationForm):
    email = forms.CharField(
        max_length=100, widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password",
                                max_length=20, widget=forms.PasswordInput(attrs={"class": "form-control mb-1"}))
    password2 = forms.CharField(label="Password Confirmation",
                                max_length=20, widget=forms.PasswordInput(attrs={"class": "form-control mb-1"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control mb-1"}),
            "last_name": forms.TextInput(attrs={"class": "form-control mb-1"}),
            "username": forms.TextInput(attrs={"class": "form-control mb-1"}),

        }
        help_texts = {
            "username": ""
        }


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadImage
        fields = ['image_name', "category", "image"]
        labels = {"image_name": "Image Name",
                  "image": "Upload Image", "category": "Image Category"}
        widgets = {
            "image_name": forms.TextInput(attrs={'class': "form-control"}),
            "category": forms.TextInput(attrs={'class': "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"})
        }
