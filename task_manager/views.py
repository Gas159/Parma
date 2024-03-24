from datetime import datetime

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, ListView

from task_manager.mixins import LoginAuthMixin
from tasks.models import Task


class IndexView(SuccessMessageMixin,  LoginAuthMixin,  ListView):
    template_name = 'index.html'
    extra_context = {'title': _('User'), 'btn': _('Create'),
                     'date': _(str((datetime.now().strftime('%B %Y'))))}
    model = Task
    context_object_name = 'tasks'
    paginate_by = 5
    def get_queryset(self):
        queryset = Task.objects.filter(executor=self.request.user)
        return queryset




    # def get_context_date(self,**kwargs):
    #     context = super().get_context_data(self, **kwargs)

    # def get_context_data(self, **kwargs):
    #     kwargs.setdefault("view", self)
    #     if self.extra_context is not None:
    #         kwargs.update(self.extra_context)
    #     return kwargs


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('Successfully login')

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(SuccessMessageMixin, LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home')
