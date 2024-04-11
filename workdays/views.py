from typing import Dict, Any

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.forms import model_to_dict

from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView

from task_manager.mixins import LoginAuthMixin
from tasks.models import Task
from workdays.forms import FilterModelForm
from workdays.mixins import WorkdayMixin
from products.models import Product
from statuses.models import Status
from workdays.models import WorkDay
from workplaces.models import Workplace

import logging

logger = logging.getLogger('main')

# Create your views here.
def toolspass(request):
    return HttpResponse("<h1> Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")


class WorkdaysListView(LoginAuthMixin, WorkdayMixin, ListView):
    template_name = 'workdays/workdays_list.html'
    context_object_name = 'workdays'
    # fields = ['name', 'description', 'workplace']
    # logger.info('hello!')
    extra_context = {
        'title': _('Workdays'), 'btn_create': _('Create Workday'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
        'menu': ['t.clear_turning_first', 't.clear_turning_second', 't.clear_turning_second']
    }


class CreateWorkdayView(SuccessMessageMixin, LoginAuthMixin, WorkdayMixin, CreateView):
    template_name = 'workdays/workday_form.html'
    success_message = _("Workday created successfully")
    error_message = _('Some went wrong')
    extra_context = {'title': _('Create workday'), 'btn': _('Create')}
    form_class = FilterModelForm
    model = WorkDay

    def get_form_kwargs(self):
        kwargs = super(CreateWorkdayView, self).get_form_kwargs()
        current_user = self.request.user
        kwargs['current_user'] = current_user
        return kwargs


    def form_valid(self, form):
        form.instance.user_name = self.request.user
        status_color = {"Выполнено": "text-success",
                        'В работе': "text-warning",
                        'Перенаплавка': "text-danger"}

        try:
            product_status = form.instance.status.name
            workplace_id = form.instance.workplace.id
            product_obj = form.instance.product

            color = status_color.get(product_status, 'Call Gas')
            dict_of_product = model_to_dict(product_obj)  # преобразует обьект в словарь
            count = 0

            for key, value in dict_of_product.items():
                if key.startswith('step'):
                    count += 1
                    if workplace_id == value:
                        setattr(product_obj, 'color_' + str(count), color)


            try:
                executor_id = form.instance.user_name.id
                task_obj = Task.objects.get(product_id=product_obj.id, workplace_id=workplace_id,
                                            executor_id=executor_id)
                task_obj.status = form.instance.status
                task_obj.status_color = color
                task_obj.save()
            except Task.DoesNotExist:
                pass

            product_obj.save()

            # print(vars(task_obj), dir(task_obj), sep='\n\n')
        except:
            pass
            # raise Exception('I dont know what need write here. Зовите Рината)')

        return super().form_valid(form)

