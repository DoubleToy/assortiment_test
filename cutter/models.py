from django.db import models
from django.utils.safestring import mark_safe

CHOICE_OF_TYPE = (
    ('Б', 'Большая'),
    ('С', 'Средняя'),
    ('М', 'Мелкая')
)


# Ежедневный план выполнения работы
class DailyProductionPlan(models.Model):
    date = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата")
    number = models.CharField(max_length=100, db_index=True, verbose_name="Номер")
    name = models.CharField(max_length=150, db_index=True, verbose_name="Наименование")
    metric = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Метраж")
    flooring = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Длина настила")
    remains = models.IntegerField(db_index=True, verbose_name="Остаток")
    defects = models.DecimalField(max_digits=5, decimal_places=2, blank=True, verbose_name="Брак")
    quantity = models.IntegerField(db_index=True, verbose_name="Количество")
    spent = models.IntegerField(verbose_name="Затрачено времени (в секундах)")

    class Meta:
        verbose_name = "Ежедневный план выпуска продукции"
        verbose_name_plural = "Ежедневный план выпуска продукций"


# Вид сырья
class TypeMaterials(models.Model):
    feedstock = models.CharField(max_length=150, db_index=True, verbose_name="Вид сырья")

    class Meta:
        verbose_name = "Вид сырья"
        verbose_name_plural = "Вид сырья"

    def __str__(self):
        return self.feedstock


# Выполняемая работа
class WorkPerformed(models.Model):
    materials = models.ForeignKey(TypeMaterials, related_name='material', on_delete=models.CASCADE,
                                verbose_name="Вид сырья")
    size = models.CharField(max_length=20, choices=CHOICE_OF_TYPE, verbose_name="Размер детали")
    spent = models.IntegerField(verbose_name="Затрачено времени (в секундах)")
    image = models.ImageField(upload_to='media/images/%Y/%m/%d/', verbose_name="Изображение", blank=True)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = "Выполненная работа"
        verbose_name_plural = "Выполненая работа"


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    quantity = models.IntegerField(verbose_name="Количество")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказ"


class TecOperation(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование операции")
    time = models.IntegerField(verbose_name="Время в секундах")

    class Meta:
        verbose_name = "Технические операции"
        verbose_name_plural = "Технические операции"


class WorkPerformedCost(models.Model):
    size = models.CharField(max_length=20, choices=CHOICE_OF_TYPE, verbose_name="Размер детали")
    cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Стоимость")

    class Meta:
        verbose_name = "Стоимость детали"
        verbose_name_plural = "Стоимость детали"

