# Generated by Django 4.0.6 on 2022-08-24 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Склад',
                'verbose_name_plural': 'Склад',
            },
        ),
    ]
