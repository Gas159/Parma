from django.db.models import Sum

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, DetailView
from django_filters.views import FilterView

from products.filters import ProductFilter
from products.mixins import ProductsMixin
from task_manager.mixins import LoginAuthMixin


def toolspass(request):
    return HttpResponse("<h1>Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")


class ProductView(LoginAuthMixin, ProductsMixin, DetailView):
    template_name = 'products/product.html'
    extra_context = {'title': _('Task'), 'btn_update': _('Update'),
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
