# Generated by Django 4.2.10 on 2024-03-23 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_color_product_color_1_and_more'),
        ('tasks', '0011_alter_task_id_alter_tasklabel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product', verbose_name='Product'),
        ),
    ]
