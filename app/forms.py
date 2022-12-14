from django.forms import ModelForm
from .models import Order, Profile,Customer
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields= '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']


class CreateProfileForm(ModelForm):
    class Meta:
        model= Customer
        fields= ['name', 'phone', 'email']