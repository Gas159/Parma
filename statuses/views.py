from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .mixins import StatusMixin


class StatusView(StatusMixin, ListView):
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Statuses'), 'btn_create': _('Create status'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }


class CreateStatusView(StatusMixin, CreateView):
    template_name = 'statuses/statuses_form.html'
    success_message = _("Status created successfully")
    extra_context = {'title': _('Create status'), 'btn': _('Create')}


class UpdateStatusView(StatusMixin, UpdateView):
    template_name = 'statuses/statuses_form.html'
    success_message = _('Status successfully changed')
    extra_context = {'title': _('Update status'), 'btn': _('Update')}


class DeleteStatusView(StatusMixin, DeleteView):
    success_message = _('Status successfully deleted')
    extra_context = {'title': _('Delete status '), 'btn_delete': _('yes, delete'), }
    error_message = _('Can\'t delete status because it\'s in use')

    def post(self, request, *args, **kwargs):
        if self.get_object().task_set.exists():
            messages.error(request, self.error_message)
            return redirect(self.success_url)
        return super().post(self, request, *args, **kwargs)
