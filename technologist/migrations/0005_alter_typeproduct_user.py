# Generated by Django 4.0.6 on 2022-09-27 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('technologist', '0004_alter_operation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
