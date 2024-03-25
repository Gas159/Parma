from typing import Dict, Any

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.forms import model_to_dict

from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.views.generic import ListView, CreateView

from task_manager.mixins import LoginAuthMixin
from tasks.models import Task
from workdays.mixins import WorkdayMixin
from products.models import Product
from statuses.models import Status


# Create your views here.
def toolspass(request):
    return HttpResponse("<h1> Здесь ничего нет, но скоро обязательно будет, наверное, ну максимум - нет:)</h1>")


class WorkdaysListView(LoginAuthMixin, WorkdayMixin, ListView):
    template_name = 'workdays/workdays_list.html'
    context_object_name = 'workdays'
    # fields = ['name', 'description', 'workplace']
    extra_context = {
        'title': _('Workdays'), 'btn_create': _('Create Workday'),
        'btn_update': _('Update'), 'btn_delete': _('Delete'),
        'menu': ['t.clear_turning_first', 't.clear_turning_second', 't.clear_turning_second']
    }


class CreateWorkdayView(SuccessMessageMixin, LoginAuthMixin, WorkdayMixin, CreateView):
    template_name = 'workdays/workday_form.html'
    success_message = _("Workday created successfully")
    error_message = _('Some went wrong')
    extra_context = {'title': _('Create workday'), 'btn': _('Create')}

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        # form.instance.author = self.request.user
        # status = form.instance.status
        # status1 = form.cleaned_data['status']

        status_color = {"Выполнено": "text-success",
                        'В работе': "text-warning",
                        'Перенаплавка': "text-danger"}

        try:
            product_status = form.instance.status.name
            workplace_id = form.instance.workplace.id
            product_obj = form.instance.product

            color = status_color.get(product_status, 'Call Gas')
            dict_of_product = model_to_dict(product_obj)  # преобразует обьект в словарь
            count = 0

            for key, value in dict_of_product.items():
                if key.startswith('step'):
                    count += 1
                    if workplace_id == value:
                        setattr(product_obj, 'color_' + str(count), color)
                        break


            try:
                executor_id = form.instance.user_name.id
                task_obj = Task.objects.get(product_id=product_obj.id, workplace_id=workplace_id,
                                                executor_id=executor_id)
                task_obj.status =  form.instance.status
                task_obj.status_color = color
                task_obj.save()
            except Task.DoesNotExist:
                pass

            product_obj.save()

            # print(Task.objects.values())
            # q = product_obj.id

            # print(task_obj, type(task_obj))
            # print(task_obj.status_color, type(task_obj.status_color))
            # print()
            # print(vars(task_obj), dir(task_obj), sep='\n\n')


        # except ValueError:
        #     return redirect('user_login')
        except:
            raise Exception('I dont know what need write here. Зовите Рината)')

        return super().form_valid(form)

    # def form_valid(self, form):
    #     form.instance.user_name = self.request.user
    #     # form.instance.author = self.request.user
    #     # status = form.instance.status
    #     # status1 = form.cleaned_data['status']
    #     operations = {"Первая чистовая операция": 'clear_turning_first',
    #                   "Вторая чистовая операция": 'clear_turning_second',
    #                   'Третья чистовая операция': 'clear_turning_third'}
    #     try:
    #
    #         operation_name = operations.get(form.instance.operation.name, 'Call admin')
    #         status = form.instance.status
    #         product = form.instance.product
    #         #print(operation_name, status, product)
    #
    #         # operation_name = form.instance.operation.name
    #         # status = form.instance.status
    #         # product = form.instance.product
    #
    #         # product = Product.objects.get(id=product_id)
    #         setattr(product, operation_name, status)
    #         product.save()
    #     except ValueError:
    #         return redirect('user_login')
    #     except:
    #         raise Exception('I dont know what need write here. Зовите Рината)')
    #
    #     return super().form_valid(form)
    # print(status, type(status), dir(status))
    # g = getattr(product, operation_name)
    # print(g, type(g))

    # print(
    #     f'operation={workday_operation}, type={type(workday_operation)},'
    #     f' status={workday_status}, type = {type(workday_status)}'
    #     f' product={product_in_workday}, type={type(workday_status)}')

    # product_in_workday.workday_operation = workday_status
    # operation_list = ['clear_turning_first', 'clear_turning_second', 'clear_turning_third']
    # product = Product.objects.get(id=product_id)
    # status_value = Status.objects.get(id=status_id)
    # setattr(product, operation_name, status_id)

    # setattr(product, operation_name, status_value)
    # g = getattr(product, operation_name)
    # print(g, type(g))
    # product_dict = {'clear_turning_first': 'product.clear_turning_first',
    #                 'clear_turning_second': 'product.clear_turning_second',
    #                 'clear_turning_third': 'product.clear_turning_third'}
    # module = __import__('Product')
    # class_object = getattr(module, "MyClass")()  # Берём класс у соседей

    # globals()['Product.objects.get(id=product_id).clear_turning_first'] = status_value

    # print(product.clear_turning_first)
    # eval(product_dict['clear_turning_first']) = status_value.name
    # exec('Product.objects.get(id=product_id)' + operation_name = status_value)
    # print(product1, type(product1))

    # t.product_dict[operation_name] = Status.objects.get(id=status_id)
    # print(f'operation name = {operation_name}, {type(operation_name)}')
    # print(f'product={p}, {type(p)}')

    # p = Status.objects.get(id=status_id)
    # product.operation_name = Status.objects.get(id=status_id)

    # print(product)
    # print(p, type(p))
    # print(operation_name, type(operation_name))

    # except ObjectDoesNotExist:
    #     print("Объект не сушествует")
    # except MultipleObjectsReturned:
    #     print("Найдено более одного объекта")

    # status1 = form.cleaned_data.get('status')
    # status2 = status1.id
    # print(status1, status2, type(status1), type(status2), sep='\n', end='\n')
    #
    # q = form.instance.product
    # print(q, type(q))
    # id1_workday = form.cleaned_data.get('product')
    # id1_workday1 = id1_workday.id
    # print(id1_workday, id1_workday1, type(id1_workday1))
    #
    # product_st = Product.objects.get(pk=id1_workday1)
    # product_st.step_1 = 'status2'
    # # product_st.status = status2
    # product_st.status = Status.objects.get(id=status2)
    # print(product_st)
    # product_st.save()
    # for operation in operation_list:
    #     if operation == 'clear_turning_first':
    #         # exec("from " + moduleName + " import " + className)
    #         exec("product1 =" + 'Product.objects.get(id=product_id).' + operation_name)
    #         print(product1, type(product1))

    # q = globals()['product.clear_turning_first']
    # q = status_value.name
    # product_dict[operation] = status_value.name
    # print()
    # product.operation = status_value
    # print(operation, type(operation))
    # print(product_dict[operation_name], type(product_dict[operation_name]))
    # product_dict[operation_name].save()
    # print(f'product first: {product}, type={type(product)}')

    # p = product_dict[operation_name]
    # produc
    # print(form)
