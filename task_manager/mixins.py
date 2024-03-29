from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

# class LoginAuthMixin():
#     pass
class LoginAuthMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('user_login')
        return super().dispatch(request, *args, **kwargs)
