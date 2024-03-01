from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.utils.translation import gettext as _

from task_manager.mixins import LoginAuthMixin
from workplaces.mixins import WorkplaceMixin
from workplaces.models import Workplace




class WorkplaceView(LoginAuthMixin, WorkplaceMixin, DetailView):  # modelname_detail.html.
    template_name = 'workplaces/workplace.html'
    extra_context = {'title': _('Workplace'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete')}
    context_object_name = 'workplace'

class WorkplacesListView(LoginAuthMixin,WorkplaceMixin, ListView):
    model = Workplace
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('workplaces')
    fields = ['name', 'description']
    template_name = 'workplaces/workplaces_list.html'
    context_object_name = 'workplaces'
    extra_context = {
        'title': _('Workplaces'), 'btn_create': _('Create Workplace'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }


class CreateWorkplaceView(SuccessMessageMixin, LoginAuthMixin, WorkplaceMixin, CreateView):
    template_name = 'workplaces/workplaces_form.html'
    success_message = _("Workplace created successfully")
    extra_context = {'title': _('Create workplace'), 'btn': _('Create')}
    model = Workplace

# class TasksListView(LoginAuthMixin, TaskMixin, FilterView):  # modelname_list.html.
#     extra_context = {'title': _('Tasks'), 'btn': _('Create task'), 'btn_update': _('Update'),
#                      'btn_delete': _('Delete'), }
#     context_object_name = 'tasks'
#     filterset_class = TaskFilter
#     template_name = 'tasks/task_list.html'

def workpass(request):
    return HttpResponse("<h1>Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")
