from django.urls import reverse_lazy

from tools.models import Tool


class ToolsMixin:
    model = Tool
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('tools')
    fields = ['name', 'description', 'workplace', 'in_supply']
