import django_filters
from labels.models import Labels
from users.models import Users
from statuses.models import Status
from tasks.models import Task
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    def show_own_task(self, queryset, arg, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    status = django_filters.ModelChoiceFilter(
        label=_('Status'),
        queryset=Status.objects.all(),
        widget=forms.Select(attrs={'class': 'm-1'})
    )
    executor = django_filters.ModelChoiceFilter(
        # label=_('Executor'),
        queryset=Users.objects.all(),
        # widget=forms.Select(attrs={'class': 'm-1'})
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Labels.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-select', }),
        label=_('Label'))

    self_task = django_filters.BooleanFilter(
        method='show_own_task',
        widget=forms.CheckboxInput(attrs={'class': 'm-2'}),
        label=_('Show own tasks'),
    )

    class Meta:
        model = Task
        fields = ['status', 'executor']
        # fields = '__all__'