from products.models import Product
from django.urls import reverse_lazy


class ProductsMixin:
    model = Product
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('products')
    fields = ['name', 'number', 'description']
    # exclude = ['step_1', 'step_2']
