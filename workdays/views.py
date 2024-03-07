from django.shortcuts import render

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView

from task_manager.mixins import LoginAuthMixin
from workdays.mixins import WorkdayMixin
from products.models import Product
from statuses.models import Status

# Create your views here.
def toolspass(request):
    return HttpResponse("<h1> Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")


class WorkdaysListView(LoginAuthMixin, WorkdayMixin, ListView):
    template_name = 'workdays/workdays_list.html'
    context_object_name = 'workdays'
    # fields = ['name', 'description', 'workplace']
    extra_context = {
        'title': _('Workdays'), 'btn_create': _('Create Workdays'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }


class CreateWorkdayView(SuccessMessageMixin, LoginAuthMixin, WorkdayMixin, CreateView):
    template_name = 'workdays/workday_form.html'
    success_message = _("Workdays created successfully")
    extra_context = {'title': _('Create workdays'), 'btn': _('Create')}

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        form.save()
        print("hello1111111111111111111111111111111111111111")
        # status = form.instance.status
        # status1 = form.cleaned_data['status']

        status1 = form.cleaned_data.get('status')
        status2 = status1.id
        print(status1, status2, type(status1), type(status2), sep='\n', end='\n')

        q = form.instance.product
        print(q, type(q))
        id1_workday = form.cleaned_data.get('product')
        id1_workday1 = id1_workday.id
        print(id1_workday, id1_workday1, type(id1_workday1))

        product_st = Product.objects.get(pk=id1_workday1)
        product_st.step_1 = 'status2'
        # product_st.status = status2
        product_st.status = Status.objects.get(id=status2)
        print(product_st)
        product_st.save()
        # print(form)
        return super().form_valid(form)




