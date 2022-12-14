# Generated by Django 4.0.6 on 2022-09-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storekeeper', '0003_warehouse_actual_warehouse_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='actual',
            field=models.IntegerField(null=True, verbose_name='Фактическое количество'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='article',
            field=models.CharField(max_length=200, null=True, verbose_name='Артикул товара'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='characteristic',
            field=models.CharField(max_length=150, null=True, verbose_name='Характеристика'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='client',
            field=models.CharField(max_length=150, null=True, verbose_name='Наименование заказчика'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='dateArrival',
            field=models.DateField(auto_now_add=True, db_index=True, null=True, verbose_name='Дата прихода'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='dateCompilation',
            field=models.DateField(db_index=True, null=True, verbose_name='Дата составления'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='documentNumber',
            field=models.CharField(max_length=200, null=True, verbose_name='Номер документа'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=150, null=True, verbose_name='Наименование товара'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='priceNDS',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Сумма без НДС'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Количество(масса нетто)'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='sort',
            field=models.CharField(max_length=150, null=True, verbose_name='Сорт'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='unit',
            field=models.CharField(max_length=200, null=True, verbose_name='Наименование еденицы измерения'),
        ),
    ]
