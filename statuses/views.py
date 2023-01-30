from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from labels.models import Labels
from .models import Status


class StatusMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Status
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('statuses')
    fields = ['name']


class StatusView(StatusMixin, ListView):
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': _('Statuses'), 'btn_create': _('Create status'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
        'id': _('ID'), 'name': _('Name'), 'create': _('Create date'),
        'update': _('Update date')
    }


class CreateStatusView(StatusMixin, CreateView):
    template_name = 'statuses/statuses_form.html'
    success_message = _("Status created successfully")
    extra_context = {'title': _('Create status'), 'btn': _('Create')}


class UpdateStatusView(StatusMixin, UpdateView):
    template_name = 'statuses/statuses_form.html'
    success_message = _('Status successfully changed')
    extra_context = {'title': _('Update status'), 'btn': _('Update')}


class DeleteStatusView(StatusMixin,  DeleteView):
    success_message = _('Status successfully deleted')
    extra_context = {'title': _('Delete status '), 'btn_delete': _('Delete status'), }

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()
            messages.success(self.request, self.success_message)
        except ProtectedError:
            if isinstance(object, Labels):
                messages.error(self.request, _('You can not delete Label which is used'))
            if isinstance(object, Status):
                messages.error(self.request, _('You can not delete Status which is used'))
        return redirect(self.success_url)
