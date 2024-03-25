# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView, DetailView

from products.mixins import ProductsMixin
from products.models import Product
from task_manager.mixins import LoginAuthMixin


class Search(LoginAuthMixin, ProductsMixin, ListView):
    template_name = 'products/products_list.html'
    extra_context = {
        'title': _('Products'), 'btn_create': _('Create product'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
    }
    context_object_name = 'products'

    paginate_by = 20

    def get_queryset(self):
        # return Product.objects.filter(number=self.request.GET.get('q'))
        # return Product.objects.filter(Q(number__contains='q') | Q(name__icontains='q'))
        value = self.request.GET.get('q')
        return Product.objects.filter(
            Q(number__icontains=value) | Q(name__icontains=value))
        # return Product.objects.all()

    def get_context_data(self, *arg, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
