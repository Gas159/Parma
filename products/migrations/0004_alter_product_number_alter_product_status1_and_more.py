# Generated by Django 4.2.10 on 2024-03-07 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0004_alter_status_id'),
        ('products', '0003_remove_product_status_remove_product_step_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='number',
            field=models.IntegerField(verbose_name='Product number'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='status1', to='statuses.status', verbose_name='Clear_1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='status2', to='statuses.status', verbose_name='Clear_2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='status3', to='statuses.status', verbose_name='Clear_3'),
        ),
    ]
