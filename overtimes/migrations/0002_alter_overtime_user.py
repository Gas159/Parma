# Generated by Django 4.2.10 on 2024-03-11 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('overtimes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Worker name'),
        ),
    ]
