from products.models import Product
from django.urls import reverse_lazy


class ProductsMixin:
    model = Product
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('products')
    fields = '__all__'
