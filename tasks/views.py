from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django_filters.views import FilterView

from task_manager.mixins import LoginAuthMixin
from .mixins import TaskMixin, TaskDeleteMixin
from tasks.filters import TaskFilter
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin


class TaskView(LoginAuthMixin, TaskMixin, DetailView):  # modelname_detail.html.
    template_name = 'tasks/task.html'
    extra_context = {'title': _('Task'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete')}
    context_object_name = 'task'


class TasksListView(LoginAuthMixin, TaskMixin, FilterView):  # modelname_list.html.
    extra_context = {'title': _('Tasks'), 'btn': _('Create task'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete'), }
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    template_name = 'tasks/task_list.html'


class CreateTaskView(SuccessMessageMixin, LoginAuthMixin, TaskMixin,
                     CreateView):  # modelname_form.html
    template_name = 'tasks/task_form.html'
    success_message = _("Task created successfully")
    extra_context = {'title': _('New Tasks'), 'btn': _('Create')}

    # Добавляем имя автора в поле author, которое не отображается в форме
    def form_valid(self, form):
        form.instance.author = self.request.user
        print("hello1111111111111111111111111111111111111111")
        return super().form_valid(form)
        


class UpdateTaskView(SuccessMessageMixin, LoginAuthMixin, TaskMixin,
                     UpdateView):  # modelname_form.html
    success_message = _('Task successfully changed')
    extra_context = {'title': _('Update task'), 'btn': _('Update')}


class DeleteTaskView(SuccessMessageMixin, TaskDeleteMixin, LoginAuthMixin, PermissionRequiredMixin,
                     TaskMixin, DeleteView):  # modelname_confirm_delete.html
    template_name = 'users/users_confirm_delete.html'
    success_message = _('Task successfully deleted')
    extra_context = {'title': _('Delete task '), 'btn_delete': _('yes, delete'), }
