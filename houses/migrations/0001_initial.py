# Generated by Django 3.2.16 on 2022-12-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('price', models.IntegerField(verbose_name='price')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
    ]