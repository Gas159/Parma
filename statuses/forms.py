from django.forms import ModelForm

from .models import Status


class StatusesChangeForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
