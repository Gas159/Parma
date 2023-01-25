from django.contrib.auth import get_user_model
from django.contrib.auth import forms
from django.forms import ModelForm

from .models import Status

class StatusesChangeForm(ModelForm):
    # username = forms.CharField(label='Логин')
    # # email = forms.EmailField(label='Email', required=False)
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='Повтор пароля',
    #                             widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = Status
        fields = ['name']