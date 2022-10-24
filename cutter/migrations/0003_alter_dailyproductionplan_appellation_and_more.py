# Generated by Django 4.0.6 on 2022-08-15 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0002_typematerials_alter_dailyproductionplan_spent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='appellation',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='date',
            field=models.DateTimeField(auto_now_add=False, db_index=False, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='defects',
            field=models.IntegerField(verbose_name='Брак'),
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='flooring',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Длина настила'),
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='metric',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Метраж'),
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='number',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='quantity',
            field=models.IntegerField(db_index=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='remains',
            field=models.IntegerField(db_index=True, verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='dailyproductionplan',
            name='spent',
            field=models.IntegerField(verbose_name='Затрачено времени'),
        ),
        migrations.AlterField(
            model_name='typematerials',
            name='feedstock',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Вид сырья'),
        ),
        migrations.AlterField(
            model_name='workperformed',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='workperformed',
            name='materials',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material', to='cutter.typematerials', verbose_name='Вид сырья'),
        ),
        migrations.AlterField(
            model_name='workperformed',
            name='size',
            field=models.CharField(choices=[('Б', 'Большая'), ('С', 'Средняя'), ('М', 'Мелкая')], max_length=20, verbose_name='Размер детали'),
        ),
        migrations.AlterField(
            model_name='workperformed',
            name='spent',
            field=models.IntegerField(verbose_name='Затрачено времени'),
        ),
    ]
