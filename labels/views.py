from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.mixins import LoginAuthMixin
from .mixins import LabelsMixin


class LabelsListView(LoginAuthMixin, LabelsMixin, ListView):  # modelname_list.html.
    extra_context = {'title': _('Labels'), 'btn': _('Create label'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete'), 'btn_create': _('Create label')}
    context_object_name = 'labels'


#
class CreateLabelView(SuccessMessageMixin, LoginAuthMixin, LabelsMixin,
                      CreateView):  # modelname_form.html
    success_message = _("Label created successfully")
    extra_context = {'title': _('New Label'), 'btn': _('Create')}


class UpdateLabelView(SuccessMessageMixin, LoginAuthMixin, LabelsMixin,
                      UpdateView):  # modelname_form.html
    success_message = _('Label successfully changed')
    extra_context = {'title': _('Update label'), 'btn': _('Update')}


#
class DeleteLabelView(SuccessMessageMixin, LoginAuthMixin, LabelsMixin,
                      DeleteView):  # modelname_confirm_delete.html
    success_message = _('Label successfully deleted')
    error_message = _('Can\'t delete label because it\'s in use')
    extra_context = {'title': _('Delete label'), 'btn_delete': _('yes, delete'), }

    def post(self, request, *args, **kwargs):
        if self.get_object().task_set.exists():
            messages.error(request, self.error_message)
            return redirect(self.success_url)
        return super().post(self, request, *args, **kwargs)
