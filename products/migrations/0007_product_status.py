# Generated by Django 4.2.10 on 2024-03-05 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0004_alter_status_id'),
        ('products', '0006_alter_product_step_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='statuses.status', verbose_name='Status'),
        ),
    ]