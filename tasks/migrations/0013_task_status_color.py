# Generated by Django 4.2.10 on 2024-03-24 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_task_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status_color',
            field=models.CharField(blank=True, max_length=222, null=True),
        ),
    ]
