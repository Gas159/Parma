# Generated by Django 4.2.10 on 2024-03-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_step_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='step_2',
            field=models.BooleanField(default=False, verbose_name='Step_2'),
        ),
    ]