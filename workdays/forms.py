from django import forms
from products.models import Product
from statuses.models import Status
from workplaces.models import Workplace
from .models import WorkDay
import logging

logger = logging.getLogger('main').debug


class FilterModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super(FilterModelForm, self).__init__(*args, **kwargs)

        if current_user:
            if Workplace.objects.filter(users=current_user).exists():
                workplace = Workplace.objects.filter(users=current_user)
                self.fields['workplace'].queryset = workplace
                self.fields['workplace'].initial = workplace[0]
                self.fields['amount'].initial = 1
                if Status.objects.filter(name='Выполнено').exists():
                    self.fields['status'].initial = Status.objects.filter(name='Выполнено')[0]

                fields = Product._meta.get_fields()
                products_queryset = Product.objects.none()
                for product in Product.objects.all():
                    for field in fields:
                        if field.name.startswith('step_'):
                            field_value = getattr(product, field.name)
                            if field_value == workplace[0]:
                                products_queryset |= Product.objects.filter(pk=product.pk)
                                break
                self.fields['product'].queryset = products_queryset

    class Meta:
        model = WorkDay
        fields = '__all__'
        exclude = ('user_name',)
        # fields = [user_name'user_name', 'workplace']
