from datetime import datetime

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse

from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView

from overtimes.mixins import OverTimeMixin
from overtimes.models import OverTime
from task_manager.mixins import LoginAuthMixin


def toolspass(request):
    return HttpResponse("<h1> Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")


class OverTimeListView( OverTimeMixin, ListView):
    template_name = 'overtimes/overtimes_list.html'
    context_object_name = 'overtimes'

    extra_context = {
        'title': _('Overtimes  ' + str(datetime.now().strftime("%B %Y"))), 'btn_create': _('Create overtime'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }

    def get_queryset(self):
        # try:
        # if self.request.user.username == 'boss':
        #     return OverTime.objects.all()
        # elif not self.request.user:
        #     return None
        # else:
        #     return OverTime.objects.filter(user=self.request.user)
        # except:

            # messages.error(request, self.error_message)
            # return redirect(self.success_url)


class CreateOvertimeView(SuccessMessageMixin, LoginAuthMixin, OverTimeMixin, CreateView):
    template_name = 'overtimes/overtime_form.html'
    success_message = _("Overtime created successfully")
    current_dateTime = datetime.now()
    extra_context = {'title': _('Create Overtime'), 'btn': _('Create')}
    error_message = _('FigVam')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user

        if OverTime.objects.filter(user=user).exists():
            OverTime.objects.get(user=self.request.user).delete()
            # raise Exception('I dont know what need write here')
            return super().form_valid(form)
        else:
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
