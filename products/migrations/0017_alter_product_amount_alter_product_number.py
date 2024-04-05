# Generated by Django 4.2.10 on 2024-04-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_number_alter_product_spec_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Кол-во'),
        ),
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.IntegerField(null=True, verbose_name='Product number'),
        ),
    ]
