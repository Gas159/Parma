# Generated by Django 4.2.10 on 2024-04-05 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_spec_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.IntegerField(default=1, null=True, verbose_name='Product number'),
        ),
        migrations.AlterField(
            model_name='product',
            name='spec_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Пункт спецификации'),
        ),
    ]
