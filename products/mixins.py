from .models import Product
from django.urls import reverse_lazy


class ProductsMixin:
    model = Product
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('products')
    fields = ['specification', 'name', 'number', 'description', 'step_1', 'step_2', 'step_3']
    # exclude = ['step_1', 'step_2']
