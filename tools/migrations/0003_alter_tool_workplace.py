# Generated by Django 4.2.10 on 2024-03-10 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workplaces', '0003_delete_createworkplaceview'),
        ('tools', '0002_tool_in_supply_alter_tool_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='workplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workplaces.workplace', verbose_name='Workplace'),
        ),
    ]