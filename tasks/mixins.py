from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.mixins import LoginAuthMixin

from .models import Task


class TaskMixin(LoginAuthMixin, SuccessMessageMixin):
    model = Task
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('tasks')
    fields = ['name', 'description', 'status', 'executor', 'labels']
