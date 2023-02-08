from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class UserMixin(UserPassesTestMixin, SuccessMessageMixin):
    def test_func(self):
        return self.get_object() == self.request.user

    def handle_no_permission(self):
        messages.error(self.request, _('You can not change another user'))
        return redirect('users')
