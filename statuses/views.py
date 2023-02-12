from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.mixins import LoginAuthMixin
from .mixins import StatusMixin


class StatusView(LoginAuthMixin, StatusMixin, ListView):
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Statuses'), 'btn_create': _('Create status'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }


class CreateStatusView(LoginAuthMixin, StatusMixin, CreateView, SuccessMessageMixin):
    template_name = 'statuses/statuses_form.html'
    success_message = _("Status created successfully")
    extra_context = {'title': _('Create status'), 'btn': _('Create')}


class UpdateStatusView(LoginAuthMixin, StatusMixin, UpdateView, SuccessMessageMixin):
    template_name = 'statuses/statuses_form.html'
    success_message = _('Status successfully changed')
    extra_context = {'title': _('Update status'), 'btn': _('Update')}


class DeleteStatusView(LoginAuthMixin, StatusMixin, DeleteView, SuccessMessageMixin):
    success_message = _('Status successfully deleted')
    extra_context = {'title': _('Delete status '), 'btn_delete': _('yes, delete'), }
    error_message = _('Can\'t delete status because it\'s in use')

    def post(self, request, *args, **kwargs):
        if self.get_object().task_set.exists():
            messages.error(request, self.error_message)
            return redirect(self.success_url)
        return super().post(self, request, *args, **kwargs)
