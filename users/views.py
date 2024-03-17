from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin

from task_manager.mixins import LoginAuthMixin
# from users.forms import RegisterUserForm
from users.models import Users
from .forms import RegisterUserForm
from .mixins import UserMixin


class UserView(ListView):
    template_name = 'users/users.html'
    model = Users
    # fields = ['email', 'first_name', 'last_name', 'password']
    # fields = ['email', 'first_name', 'last_name', 'password']
    context_object_name = 'users'
    extra_context = {'title': _('Users'), 'btn_update': _('Update'), 'btn_delete': _('Delete')}
    redirect_field_name = 'home'


class RegisterUserView(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    model = Users
    # fields = ['email']
    template_name = 'users/register.html'
    success_url = reverse_lazy('user_login')
    success_message = _('User successfully registered')
    extra_context = {'title': _('Registration user'),
                     'btn_name': _('Register')
                     }


class UpdateUserView(LoginAuthMixin, UserMixin, UpdateView):
    model = Users
    # fields = ['email', 'first_name', 'last_name', 'password']
    # model = get_user_model()
    # form_class = RegisterUserForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('users')
    success_message = _('User successfully changed')
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'), }


class DeleteUserView(LoginAuthMixin, UserMixin, DeleteView):
    model = Users
    fields = ['email', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
    extra_context = {'title': _('Delete user'),
                     'btn_delete': _('yes, delete'), }
    error_message = _('Невозможно удалить пользователя, потому что он используется')

    def post(self, request, *args, **kwargs):
        if self.get_object().task_set.exists():
            messages.error(request, self.error_message)
            return redirect(self.success_url)
        return super().post(self, request, *args, **kwargs)
