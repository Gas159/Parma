from django.utils.translation import gettext as _
from .models import Labels
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class LabelsMixin(LoginRequiredMixin, SuccessMessageMixin):
    model = Labels
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('labels')
    fields = ['name']


class LabelsListView(LabelsMixin, ListView):  # modelname_list.html.
    extra_context = {'title': _('Labels'), 'btn': _('Create label'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete'), 'btn_create': _('Create label')}
    context_object_name = 'labels'


#
class CreateLabelView(LabelsMixin, CreateView):  # modelname_form.html
    success_message = _("Label created successfully")
    extra_context = {'title': _('New Label'), 'btn': _('Create')}

    # def form_valid(self, form):
    #     # form.instance.author = Users.objects.get(id=self.request.user.id)
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class UpdateLabelView(LabelsMixin, UpdateView):  # modelname_form.html
    success_message = _('Label successfully changed')
    extra_context = {'title': _('Update label'), 'btn': _('Update')}


#
class DeleteLabelView(LabelsMixin, DeleteView):  # modelname_confirm_delete.html
    success_message = _('Label successfully deleted')
    extra_context = {'title': _('Delete label '), 'btn_delete': _('Delete'), }
