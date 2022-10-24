from django.db import models
from django.utils.safestring import mark_safe
from cutter.models import Order
from django.urls import reverse


class Warehouse(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование товара", null=True)
    quantity = models.IntegerField(verbose_name="Количество(масса нетто)", null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    unit = models.CharField(max_length=200, verbose_name="Наименование еденицы измерения", null=True)
    characteristic = models.CharField(max_length=150, verbose_name="Характеристика", null=True)
    sort = models.CharField(max_length=150, verbose_name="Сорт", null=True)
    article = models.CharField(max_length=200, verbose_name="Артикул товара", null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена",null=True)
    priceNDS = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Сумма без НДС",null=True)
    dateArrival = models.DateField(auto_now_add=True, db_index=True, verbose_name="Дата прихода", null=True)
    client = models.CharField(max_length=150, verbose_name="Наименование заказчика", null=True)
    documentNumber = models.CharField(max_length=200, verbose_name="Номер документа", null=True)
    dateCompilation = models.DateField(db_index=True, verbose_name="Дата составления", null=True)
    image = models.ImageField(upload_to='media/images/%Y/%m/%d/', verbose_name="Изображение", null=True)
    actual = models.IntegerField(verbose_name="Фактическое количество", null=True)


    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склад"

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'


class UpFile(models.Model):
    xlsfile = models.FileField(upload_to='media/xls/%Y/%m/%d/', verbose_name="Файл", null=True)

    class Meta:
        verbose_name = "Загрузка файла"
        verbose_name_plural = "Загрузка файла"