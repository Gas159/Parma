from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# from users.models import Users

class RegisterUserForm(UserCreationForm):
    # username = forms.CharField(label='Логин')
    # # email = forms.EmailField(label='Email', required=False)
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Повтор пароля',
    #                             widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name']

# class UpdateUser()
