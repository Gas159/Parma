from django.urls import reverse_lazy
from .models import Status


class StatusMixin:
    model = Status
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('statuses')
    fields = ['name']
