# Generated by Django 3.2.16 on 2022-12-19 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_auto_20221214_0819'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
