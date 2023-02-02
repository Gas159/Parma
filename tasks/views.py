from django.utils.translation import gettext as _
from django_filters.views import FilterView
from tasks.filters import TaskFilter
from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Task


class TaskMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Task
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('tasks')
    fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskView(TaskMixin, DetailView):  # modelname_detail.html.
    template_name = 'tasks/task.html'
    extra_context = {'title': _('Task'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete')}
    context_object_name = 'task'


class TasksListView(TaskMixin, FilterView):  # modelname_list.html.
    extra_context = {'title': _('Tasks'), 'btn': _('Create task'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete'), }
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    template_name = 'tasks/task_list.html'


class CreateTaskView(TaskMixin, CreateView):  # modelname_form.html
    template_name = 'tasks/task_form.html'
    success_message = _("Task created successfully")
    extra_context = {'title': _('New Tasks'), 'btn': _('Create')}

    # Добавляем имя автора в поле author, которое не отображается в форме
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(TaskMixin, UpdateView):  # modelname_form.html
    success_message = _('Task successfully changed')
    extra_context = {'title': _('Update task'), 'btn': _('Update')}


class DeleteTaskView(TaskMixin, DeleteView):  # modelname_confirm_delete.html UserPassesTestMixin
    template_name = 'users/users_confirm_delete.html'
    success_message = _('Task successfully deleted')
    extra_context = {'title': _('Delete task '), 'btn_delete': _('yes, delete'), }

    def get(self, request, *args, **kwargs):
        author = self.get_object().author
        if author == self.request.user:
            return super().get(self, request, *args, **kwargs)
        messages.error(self.request, _('Only author can delete task'))
        return redirect('tasks')
