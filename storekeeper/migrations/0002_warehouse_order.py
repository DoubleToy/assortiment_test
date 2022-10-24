# Generated by Django 4.0.6 on 2022-08-24 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0009_order_alter_dailyproductionplan_defects_and_more'),
        ('storekeeper', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cutter.order'),
        ),
    ]
