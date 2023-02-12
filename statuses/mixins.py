from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Status


class StatusMixin(SuccessMessageMixin):
    model = Status
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('statuses')
    fields = ['name']
