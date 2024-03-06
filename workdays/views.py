from django.shortcuts import render

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView

from task_manager.mixins import LoginAuthMixin
from workdays.mixins import WorkdayMixin


# Create your views here.
def toolspass(request):
    return HttpResponse("<h1> Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")

class WorkdaysListView(LoginAuthMixin, WorkdayMixin, ListView):
    template_name = 'workdays/workdays_list.html'
    context_object_name = 'workdays'
    # fields = ['name', 'description', 'workplace']
    extra_context = {
        'title': _('Workdays'), 'btn_create': _('Create Workdays'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }
class CreateWorkdayView(SuccessMessageMixin, LoginAuthMixin, WorkdayMixin, CreateView):
    template_name = 'workdays/workday_form.html'
    success_message = _("Workdays created successfully")
    extra_context = {'title': _('Create workdays'), 'btn': _('Create')}