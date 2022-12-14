# Generated by Django 4.0.6 on 2022-08-03 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeMaterials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedstock', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='spent',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='WorkPerformed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=100)),
                ('spent', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material', to='cutter.typematerials')),
            ],
        ),
    ]
