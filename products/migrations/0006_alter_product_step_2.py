# Generated by Django 4.2.10 on 2024-03-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_step_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='step_2',
            field=models.BooleanField(default='', verbose_name='Step_2'),
        ),
    ]