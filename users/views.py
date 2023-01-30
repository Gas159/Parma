from django.utils.translation import gettext as _

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model

from django.contrib.messages.views import SuccessMessageMixin
from users.forms import RegisterUserForm
from users.models import Users


class UserView(ListView):
    template_name = 'users/users.html'
    model = Users
    context_object_name = 'users'
    extra_context = {'title': _('Users'), 'btn_update': _('Update'), 'btn_delete': _('Delete')}
    redirect_field_name = 'home'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)  # take initial context
    #     # c_def = self.get_user_context(title='Главная страница')
    #     # context['menu'] = menu
    #     # context['title'] = 'Главная страница'
    #     # context['cat_selected'] = 0
    #     return context
    # #
    # def get_queryset(self):  # будет показано если опубликовано
    #     return User.objects.filter(is_published=True).select_related(
    #         'cat')  # жадная загрузка для уменьшения повторных sql запросов


class RegisterUserView(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'  # link on template
    success_url = reverse_lazy('user_login')  # redirect
    success_message = _('User successfully registered')
    extra_context = {'title': _('Registration user'),
                     'btn_name': _('Register')
                     }


class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = get_user_model()
    form_class = RegisterUserForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('users')
    success_message = _('User successfully changed')
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'),
                     }


class DeleteUserView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Users
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
    extra_context = {'title': _('Delete user'),
                     'btn_delete': _('Delete'),
                     }
