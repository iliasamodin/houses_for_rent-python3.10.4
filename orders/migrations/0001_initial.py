# Generated by Django 3.2.16 on 2022-12-19 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0003_auto_20221214_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('client_phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('application_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи заявки')),
                ('house_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='houses.house', verbose_name='Дом')),
            ],
        ),
    ]