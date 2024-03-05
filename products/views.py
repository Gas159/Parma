from django.shortcuts import render

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView

from products.mixins import ProductsMixin
from task_manager.mixins import LoginAuthMixin
from tools.mixins import ToolsMixin

def toolspass(request):
    return HttpResponse("<h1>Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")

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

