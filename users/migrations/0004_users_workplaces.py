# Generated by Django 4.2.10 on 2024-03-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_options_alter_users_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='workplaces',
            field=models.IntegerField(blank=True, null=True, verbose_name='workplaces'),
        ),
    ]