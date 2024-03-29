# Generated by Django 4.2.10 on 2024-03-09 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0004_alter_status_id'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status1', to='statuses.status', verbose_name='status1'),
        ),
        migrations.AddField(
            model_name='product',
            name='status_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status2', to='statuses.status', verbose_name='status2'),
        ),
        migrations.AddField(
            model_name='product',
            name='status_3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status3', to='statuses.status', verbose_name='status3'),
        ),
    ]
