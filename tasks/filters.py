import django_filters
from labels.models import Labels
from tasks.models import Task
from django import forms
from django.utils.translation import gettext_lazy as _

class TaskFilter(django_filters.FilterSet):
    def show_own_task(self, queryset, arg, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    labels = django_filters.ModelChoiceFilter(
        queryset=Labels.objects.all(),
        # label=_('Label filter'),
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )

    self_task = django_filters.BooleanFilter(
        method='show_own_task',
        widget=forms.CheckboxInput,
        label=_('Show own tasks'),
        # field_name='author',
    )


    class Meta:
        model = Task
        fields = ['status', 'executor']