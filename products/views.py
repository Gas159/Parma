from django.db.models import Sum

from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, DetailView

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
        # try:
        object = super(ProductView, self).get_object()
        obj_simple = object.workday_set
        object.order = obj_simple.all().order_by('created_at')
        operation_names = set([i.workplace_name for i in obj_simple.all()])
        operation_list = {}
        for operation in operation_names:
            total_sum = obj_simple.filter(workplace_name=operation).aggregate(total=Sum('time'))
            print(total_sum, type(total_sum))
            # name = object.workday_set.filter(workplace_name=operation)[0].workplace_name.name
            operation_list[operation] = total_sum['total']
        operation_list['total_time'] = obj_simple.aggregate(total=Sum('time'))['total']
        delta_time_for_treatment = object.update_at - object.created_at
        object.delta_time = delta_time_for_treatment

        object.total = operation_list

        return object


class ProductsListView(LoginAuthMixin, ProductsMixin, ListView):
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    # fields = ['name', 'description', 'workplace']
    extra_context = {
        'title': _('Products'), 'btn_create': _('Create product'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }


class CreateProductView(SuccessMessageMixin, LoginAuthMixin, ProductsMixin, CreateView):
    template_name = 'products/product_form.html'
    success_message = _("Products created successfully")
    extra_context = {'title': _('Create product'), 'btn': _('Create')}
