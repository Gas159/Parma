# Generated by Django 4.2.10 on 2024-03-01 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workplaces', '0003_delete_createworkplaceview'),
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='in_supply',
            field=models.CharField(blank=True, default='В наличии', max_length=222, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='description',
            field=models.TextField(max_length=333, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='tool',
            name='workplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='workplaces.workplace', verbose_name='Workplace'),
        ),
    ]
