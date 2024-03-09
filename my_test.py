from products.models import Product

# product_id = 15
operation_name ='clear_turning_first'

# product = Product.objects.get(id=product_id)
# print(f'product first: {product}')
product_dict = {'clear_turning_first': 'clear_turning_first',
                'clear_turning_second': 'product.clear_turning_second',
                'clear_turning_third': 'product.clear_turning_third'}
p = product_dict[operation_name]
print(f'operation name = {operation_name}, {type(operation_name)}')
print(f'product={p}, {type(p)}')

{% for s in menu %}
        {% if t.clear_turning_first %}
        <td> <p color="green"> {{t.clear_turning_first}} </p> </td>
        {% else %}
        <td> </td>
        {% endif %}

        {% if t.clear_turning_second %}
        <td> <p color="green"> {{t.clear_turning_second}} </p> </td>
        {% else %}
        <td></td>
        {% endif %}

        {% if t.clear_turning_third %}
        <td> <p color="green"> {{t.clear_turning_third}} </p> </td>
        {% else %}
        <td></td>
<!--        <td><a class="text-danger"/> {{t.step_2}}</td>-->
        {% endif %}
          {% endif %}