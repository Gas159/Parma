from django.urls import reverse_lazy
from workdays.models import WorkDay


class WorkdayMixin:
    model = WorkDay
    login_url = reverse_lazy('user_login')
    success_url = reverse_lazy('workdays')
    fields = [ 'product', 'workplace_name', 'time', 'operation', 'status', 'description']
