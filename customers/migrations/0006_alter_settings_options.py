# Generated by Django 4.0.6 on 2022-08-16 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20220816_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Настройки', 'verbose_name_plural': 'Настройки'},
        ),
    ]