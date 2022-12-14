# Generated by Django 4.0.6 on 2022-08-16 07:05

from django.db import migrations
from customers.models import Settings


def add_cost(apps, schema_editor):
    customers = Settings()
    customers.name = 'Стоймость одной секунды'
    customers.value = '100'
    customers.save()


def remove_cost(apps, schema_editor):
    Settings.objects.filter(name='cost').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_remove_settings_cost_settings_name_settings_value'),
    ]

    operations = [
        migrations.RunPython(add_cost, remove_cost)
    ]
