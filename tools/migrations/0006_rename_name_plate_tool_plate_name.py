# Generated by Django 4.2.10 on 2024-03-30 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_tool_d_tool_l_tool_lc_tool_r_tool_z_tool_company_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='name_plate',
            new_name='plate_name',
        ),
    ]
