# Generated by Django 4.2.10 on 2024-03-09 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_status_1_product_status_2_product_status_3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='status_1',
            new_name='clear_turning_first',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='status_2',
            new_name='clear_turning_second',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='status_3',
            new_name='clear_turning_third',
        ),
    ]