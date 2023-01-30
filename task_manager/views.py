from django.contrib.messages.views import SuccessMessageMixin

from django.utils.translation import gettext as _
from django.shortcuts import redirect

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth import logout

from django.views.generic import TemplateView


class IndexView(SuccessMessageMixin, TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('User'), 'btn': _('Create')}


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('Successfully login')

    def get_success_url(self):
        return reverse_lazy('home')


def logout_view(request):
    logout(request)
    return redirect('home')
