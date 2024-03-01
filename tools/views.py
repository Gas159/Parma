from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView

from task_manager.mixins import LoginAuthMixin
from tools.mixins import ToolsMixin


# Create your views here.
def toolspass(request):
    return HttpResponse("<h1>Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")

class ToolsListView(LoginAuthMixin, ToolsMixin, ListView):
    template_name = 'tools/tools_list.html'
    context_object_name = 'tools'
    # fields = ['name', 'description', 'workplace']
    extra_context = {
        'title': _('Tools'), 'btn_create': _('Create Tools'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }
class CreateToolView(SuccessMessageMixin, LoginAuthMixin, ToolsMixin, CreateView):
    template_name = 'tools/tool_form.html'
    success_message = _("Tool created successfully")
    extra_context = {'title': _('Create tool'), 'btn': _('Create')}

