# Generated by Django 4.2.10 on 2024-03-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_color_4_product_color_5_product_color_6_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1, null=True, verbose_name='Кол-во'),
        ),
    ]
