from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


# from users.models import Users

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name']
        # fields = '__all__'
# class UpdateUser()
