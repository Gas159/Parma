from django.urls import reverse_lazy
from .models import Workplace


class WorkplaceMixin:
    model = Workplace
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('workplaces')
    fields = ['name', 'description']
