import logging

from django.db.models import Sum

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, DetailView
from django_filters.views import FilterView

from products.filters import ProductFilter
from products.mixins import ProductsMixin
from products.models import Product
from statuses.models import Status
from task_manager.mixins import LoginAuthMixin
from tasks.models import Task
from workplaces.models import Workplace

logger = logging.getLogger('main')


def toolspass(request):
    return HttpResponse("<h1>Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")


class ProductView(LoginAuthMixin, ProductsMixin, DetailView):
    template_name = 'products/product.html'
    extra_context = {'title': _('Product'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete')}
    context_object_name = 'product'

    def get_object(self, queryset=None):
        object = super(ProductView, self).get_object()
        obj_simple = object.workday_set
        object.order = obj_simple.all().order_by('created_at')
        operation_names = set([i.workplace for i in obj_simple.all()])
        operation_list = {}
        for operation in operation_names:
            total_sum = obj_simple.filter(workplace=operation).aggregate(total=Sum('time'))
            operation_list[operation] = total_sum['total']
        operation_list['total_time'] = obj_simple.aggregate(total=Sum('time'))['total']
        object.delta_time = object.update_at - object.created_at
        object.total = operation_list
        return object


class ProductStageView(LoginAuthMixin, ProductsMixin, DetailView):
    template_name = 'products/product_stage.html'
    extra_context = {'title': _('Workplace'), 'btn_update': _('Update'),
                     'btn_delete': _('Delete')}
    context_object_name = 'product_stage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            stage_id = self.request.GET.get('stage_id')
            context['stage_id'] = stage_id
        except:
            pass
        finally:
            return context

    def get_object(self, queryset=None):
        object = super(ProductStageView, self).get_object()


        obj_simple = object.workday_set
        object.order = obj_simple.all().order_by('created_at')
        operation_names = set([i.workplace for i in obj_simple.all()])
        operation_list = {}
        for operation in operation_names:
            total_sum = obj_simple.filter(workplace=operation).aggregate(total=Sum('time'))
            operation_list[operation] = total_sum['total']
        operation_list['total_time'] = obj_simple.aggregate(total=Sum('time'))['total']
        object.delta_time = object.update_at - object.created_at
        object.total = operation_list
        # object.workplace = obj_simple.filter(id=self.request.GET.get('stage_id')) #1
        object.workplace = obj_simple.filter(workplace=self.request.GET.get('stage_id'))
        return object


class ProductsListView(LoginAuthMixin, ProductsMixin, FilterView, ListView):
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    filterset_class = ProductFilter
    extra_context = {
        'title': _('Products'), 'btn_create': _('Create product'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }


class CreateProductView(SuccessMessageMixin, LoginAuthMixin, ProductsMixin, CreateView):
    template_name = 'products/product_form.html'
    success_message = _("Products created successfully")
    extra_context = {'title': _('Create product'), 'btn': _('Create')}

    def form_valid(self, form):
        ''' Пробегаем по полям продукции. Ищем раб места и создаем на каждое задачу'''
        response = super().form_valid(form)
        workplaces = Workplace.objects.all()
        # logger.debug(workplaces)
        # logger.debug(response)
        for field in [f.name for f in Product._meta.get_fields()]:
            # logger.debug(field)
            # logger.debug(getattr(form.instance, field, 'pass'))
            # logger.debug(' ')
            workplace = getattr(form.instance, field, 'pass')
            if workplace in workplaces:
                Task.objects.create(workplace=workplace,
                                    product=form.instance,
                                    author=self.request.user,
                                    status=Status.objects.get(name='Взять в работу'))
                logger.info(f'Task {workplace} created')
        return response
