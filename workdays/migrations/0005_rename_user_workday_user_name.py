# Generated by Django 4.2.10 on 2024-03-07 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workdays', '0004_workday_workplace_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workday',
            old_name='user',
            new_name='user_name',
        ),
    ]