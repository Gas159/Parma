from django import forms

from products.models import Product
from users.models import Users
from workplaces.models import Workplace
from .models import WorkDay


class FilterModelForm(forms.ModelForm):
    filter_value = forms.CharField(label='Filter')
    workplace = forms.ModelChoiceField(queryset=Workplace.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.none())

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super(FilterModelForm, self).__init__(*args, **kwargs)

        if current_user:
            # print(Workplace.objects.filter(users=current_user).exists(),
            # type(Workplace.objects.filter(users=current_user)))
            if Workplace.objects.filter(users=current_user).exists():
                workplace = Workplace.objects.filter(users=current_user)
                self.fields['workplace'].queryset = workplace

                print(Product.objects.filter(step_5=workplace[0]).exists())

                # if Product.objects.filter(step_5=workplace[0]).exists():
                #
                #     self.fields['product'].queryset = Product.objects.filter(step_5=workplace[0])

                workplace = workplace[0]  # Предполагается, что workplace - это объект Workplace, а не список


                # Получаем все поля модели Product
                product_fields = Product._meta.get_fields()

                # Создаем пустой queryset, в который будем добавлять продукты, соответствующие условиям
                filtered_products = Product.objects.none()

                # Проходимся по полям модели Product
                for field in product_fields:
                    # Получаем значение поля
                    field_value = getattr(workplace, field.name, None)
                    if field_value is not None:
                        # Создаем фильтр для текущего поля и значения workplace
                        filter_kwargs = {field.name: field_value}
                        # Фильтруем продукты и добавляем их к общему queryset
                        filtered_products |= Product.objects.filter(**filter_kwargs)

                # Устанавливаем полученный queryset для поля 'product'
                self.fields['product'].queryset = filtered_products
    class Meta:
        model = WorkDay
        fields = '__all__'
        exclude = ('user_name',)
        # fields = [user_name'user_name', 'workplace']

    #
    # def filter_queryset(self, queryset):
    #     filter_value = self.cleaned_data.get('user_name')
    #     if filter_value:
    #         queryset = queryset.filter(workplace__icontains=filter_value)
    #         print('dfasfdafda')
    #     return queryset
    #
    # def filter_queryset(self, queryset):
    #     # Get the selected user name from the form
    #     filter_value = self.cleaned_data.get('user_name')
    #     # filter_value = self.get_object()
    #     print(filter_value)
    #     # If a user name is selected, filter the Workplace queryset based on it
    #     if filter_value:
    #         # Filter the Workplace queryset to get related instances based on the selected user name
    #         workplaces = Workplace.objects.filter(users__user_name=filter_value)
    #         print('workplaces')
    #
    #         # Extract the IDs of the filtered workplaces
    #         workplace_ids = [workplace.id for workplace in workplaces]
    #
    #         # Filter the original queryset based on the filtered workplace IDs
    #         queryset = queryset.filter(workplace__id__in=workplace_ids)
    #
    #     return queryset
