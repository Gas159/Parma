from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView


class IndexView(SuccessMessageMixin, TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('User'), 'btn': _('Create')}


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

    # def get_success_url(self):
    #     messages.warning(self.request, _('Successfully logout'))
    #     return reverse_lazy('home')

