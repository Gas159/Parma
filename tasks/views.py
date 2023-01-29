from django.shortcuts import render
from django.utils.translation import gettext as _
from django_filters.views import FilterView
from tasks.filters import TaskFilter
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.contrib.auth import logout, login, get_user_model
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from users.models import Users
from users.forms import RegisterUserForm
from .models import Task

{
    'title': _('Statuses'), 'btn_create': _('Create status'),
    'btn_update': _('Update'), 'btn_delete': _('Delete'),
    'id': _('ID'), 'name': _('Name'), 'create': _('Create date'),
    'update': _('Update date')
}


class TaskMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Task
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('tasks')
    # extra_context = {'title': _('New Tasks'), 'btn': _('Create')}
    fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskView(TaskMixin, DetailView):  # modelname_detail.html.
    template_name = 'tasks/task.html'
    extra_context = {'title': _('Task'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete')}
    context_object_name = 'task'


class TasksListView(TaskMixin, ListView):  # modelname_list.html.
    # template_name = 'tasks/tasks_list.html'
    extra_context = {'title': _('Tasks'), 'btn': _('Create task'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete'), }
    context_object_name = 'tasks'
    # filterset_class = TaskFilter


class CreateTaskView(TaskMixin, CreateView):  # modelname_form.html
    template_name = 'tasks/task_form.html'
    success_message = _("Task created successfully")
    extra_context = {'title': _('New Tasks'), 'btn': _('Create')}

    def form_valid(self, form):
        # form.instance.author = Users.objects.get(id=self.request.user.id)
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(TaskMixin, UpdateView):  # modelname_form.html
    # template_name = 'tasks/task_form.html'
    success_message = _('Task successfully changed')
    extra_context = {'title': _('Update task'), 'btn': _('Update')}


class DeleteTaskView(TaskMixin, UserPassesTestMixin, DeleteView):  # modelname_confirm_delete.html
    template_name = 'users/users_confirm_delete.html'
    success_message = _('Task successfully deleted')
    extra_context = {'title': _('Delete task '), 'btn_delete': _('Delete'), }

    # self.get_object()

    # def test_func(self):
    #     task_id = self.get_object().id # берем айди
    #     author = Task.objects.get(id=task_id).author.id
    #     return author == self.request.user.id
    def test_func(self):
        # task_id = self.get_object().id
        author = Task.objects.get(id=self.get_object().id).author
        return author == self.request.user

    def handle_no_permission(self):
        messages.warning(self.request, _('Only author can delete task'))
        return redirect(reverse_lazy('tasks'))
