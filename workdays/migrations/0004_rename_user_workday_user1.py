# Generated by Django 4.2.10 on 2024-03-06 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workdays', '0003_alter_workday_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workday',
            old_name='user',
            new_name='user1',
        ),
    ]
