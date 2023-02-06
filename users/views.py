from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import RegisterUserForm
from users.models import Users
from django.contrib.auth import login
from django.shortcuts import redirect



class UserMixin(UserPassesTestMixin, SuccessMessageMixin):
    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, _('You can not change another user'))
            return redirect('users')
        else:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('user_login')



class UserView(ListView):
    template_name = 'users/users.html'
    model = Users
    context_object_name = 'users'
    extra_context = {'title': _('Users'), 'btn_update': _('Update'), 'btn_delete': _('Delete')}
    redirect_field_name = 'home'


class RegisterUserView(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('user_login')
    success_message = _('User successfully registered')
    extra_context = {'title': _('Registration user'),
                     'btn_name': _('Register')
                     }


class UpdateUserView(LoginRequiredMixin, UserMixin, UpdateView):
    model = get_user_model()
    form_class = RegisterUserForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('users')
    success_message = _('User successfully changed')
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'), }

    def form_valid(self, form):
        """If the form is valid, save the associated model and log the user in."""
        user = form.save()
        login(self.request, user)
        messages.info(self.request, self.success_message)
        return redirect(self.success_url)


class DeleteUserView(LoginRequiredMixin, UserMixin,  DeleteView):
    model = Users
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
    extra_context = {'title': _('Delete user'),
                     'btn_delete': _('yes, delete'), }
