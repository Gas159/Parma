# Generated by Django 4.2.10 on 2024-03-22 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_status_1_product_clear_turning_first_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.IntegerField(blank=True, null=True, verbose_name='Specification'),
        ),
    ]
