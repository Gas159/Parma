from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from overtimes.models import OverTime
from django.utils.translation import gettext as _


class OverTimeMixin:
    model = OverTime
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('overtimes')
    fields = ['time']


class OvertimeCreateMixin:
    def has_permission(self):
        return self.get_object().user == self.request.user

    def handle_no_permission(self):
        messages.error(
            self.request, _('Your record is exist. Please click "Update" button. ')
        )
        return redirect('overtimes')
