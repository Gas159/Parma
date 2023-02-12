from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Task
from django.utils.translation import gettext as _


class TaskMixin(SuccessMessageMixin):
    model = Task
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('tasks')
    fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskDeleteMixin():
    def has_permission(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(
            self.request, _('Only author can delete task')
        )
        return redirect('tasks')
