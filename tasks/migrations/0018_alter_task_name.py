# Generated by Django 4.2.10 on 2024-04-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_alter_task_executor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Task name'),
        ),
    ]