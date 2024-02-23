from django.forms import ModelForm

from .models import Workplace

class WorkplaceChangeForm(ModelForm):
    class Meta:
        model = Workplace
        fields = ['name', 'description']

