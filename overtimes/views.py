from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView

from overtimes.mixins import OverTimeMixin, OvertimeCreateMixin
from overtimes.models import OverTime
from task_manager.mixins import LoginAuthMixin


def toolspass(request):
    return HttpResponse("<h1> Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")


class OverTimeListView(LoginAuthMixin, OverTimeMixin, ListView):
    template_name = 'overtimes/overtimes_list.html'
    context_object_name = 'overtimes'
    extra_context = {
        'title': _('Overtimes  ' + str(datetime.now().strftime("%B %Y"))), 'btn_create': _('Create overtime'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }


class CreateOvertimeView(SuccessMessageMixin, LoginAuthMixin, OverTimeMixin, CreateView):
    template_name = 'overtimes/overtime_form.html'
    success_message = _("Overtime created successfully")
    current_dateTime = datetime.now()
    extra_context = {'title': _('Create Overtime'), 'btn': _('Create')}
    error_message = _('FigVam')

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            user = self.request.user
            user_check = OverTime.objects.get(user=user)
            if not user_check:
                messages.error(
                    self.request, _('Your record is exist. Please click "Update" button. ')
                )
                return redirect('overtimes')
            else:
                user_check.delete()
                return super().form_valid(form)
        except ObjectDoesNotExist:
            print('2111111111111')
            return super().form_valid(form)

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     try:
    #         user = self.request.user
    #         OverTime.objects.get(user=user)
    #         messages.error(
    #             self.request, _('Your record is exist. Please click "Update" button. ')
    #         )
    #         return redirect('overtimes')
    #     except :
    #         return super().form_valid(form)
