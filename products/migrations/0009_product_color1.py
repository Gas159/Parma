# Generated by Django 4.2.10 on 2024-03-23 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color1',
            field=models.CharField(blank=True, max_length=29, null=True),
        ),
    ]