import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from products.models import Product
from statuses.models import Status


class ProductFilter(django_filters.FilterSet):
    # name = django_filters.CharFilter(
    #     label=_('Specification'), widget=forms.Select(attrs={'class': 'm-1'}))
    # status = django_filters.ModelChoiceFilter(
    #     label=_('Status'),
    #     queryset=Status.objects.all(),
        # widget=forms.Select(attrs={'class': 'm-1'})
    # )
    specification = django_filters.AllValuesFilter(label='Specification', lookup_expr='iexact')
    name = django_filters.AllValuesFilter(label='Name', lookup_expr='iexact')

    order_by_specification = django_filters.OrderingFilter(label='Order by spec',
        fields=(('specification', 'specification')))
    # order_by_name = django_filters.OrderingFilter( label='Oreder by name',
    #     fields=(('name', 'name')))


    # username = rest_framework.CharFilter(field_name='user__username',
    # lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['specification', 'name']
        ordering = ['-name']

        # fields = '__all__'
        # 'specification',
