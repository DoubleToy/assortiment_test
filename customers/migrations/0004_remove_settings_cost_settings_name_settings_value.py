# Generated by Django 4.0.6 on 2022-08-16 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20220816_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='cost',
        ),
        migrations.AddField(
            model_name='settings',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='value',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
