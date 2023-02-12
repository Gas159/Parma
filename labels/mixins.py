from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Labels


class LabelsMixin(SuccessMessageMixin):
    model = Labels
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('labels')
    fields = ['name']
