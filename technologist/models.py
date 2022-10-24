from django.db import models
from django.contrib.auth.models import User
from seamstress.models import Hours

CHOICE_OF_TYPE = (
    ('Сл', 'Сложная'),
    ('Ср', 'Средняя'),
    ('Ле', 'Легкая')
)


class TypeProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Швеи", blank=True)
    type_products = models.CharField(max_length=150, db_index=True, verbose_name="Вид продукции")
    type_work = models.CharField(max_length=20, choices=CHOICE_OF_TYPE, verbose_name="Вид работы")
    quantity = models.IntegerField(verbose_name="Необходимое количество")
    period = models.IntegerField(verbose_name="Срок выполнения", blank=True, null=True)
    time = models.IntegerField(verbose_name="Срок выполнения(в секундах)", blank=True, null=True)
    hour = models.ForeignKey(Hours, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Вид продукции"
        verbose_name_plural = "Вид продукции"


class Operation(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    time = models.IntegerField(verbose_name="Время в секундах")
    spent = models.IntegerField(verbose_name="Стоймость")

    class Meta:
        verbose_name = "Операция"
        verbose_name_plural = "Операция"

    def __str__(self):
        return self.name


class TechnicalProcess(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")

    class Meta:
        verbose_name = "Технический процесс"
        verbose_name_plural = "Технический процесс"


class SelectionOperation(models.Model):
    number = models.IntegerField(verbose_name="Порядковый номер")
    operation = models.ForeignKey(Operation, related_name="Операция", on_delete=models.CASCADE, verbose_name="Операция")
    time = models.IntegerField(verbose_name="Время в секундах")
    seamstress = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Швея")
    tec_process = models.ForeignKey(TechnicalProcess, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Выбор операции"
        verbose_name_plural = "Выбор операции"


class Order(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование изделия")


    class Meta:
        verbose_name = "Изделия"
        verbose_name_plural = "Изделия"


class Expenses(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    waste = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Нормы расхода")
    unit = models.CharField(max_length=255, verbose_name="Ед. изм.")
    total = models.DecimalField(max_digits=15, decimal_places=3, verbose_name="Итого")
    order_expenses = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Нормы расхода"
        verbose_name_plural = "Нормы расхода"


class OrderAny(models.Model):
    body = models.CharField(max_length=255, verbose_name="Размер / рост")
    quantity = models.IntegerField(verbose_name="Количество (комплектов, пар, штук)")
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Цена изготовления одной ед. продукции, "
                                                                             "руб.")
    cost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Стоимость изготовления продукции, руб.")
    totalQ = models.IntegerField(verbose_name="Итого: Количество (комплектов, пар, штук)")
    totalC = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Итого: Стоимость изготовления "
                                                                               "продукции, руб.")
    order_expenses = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Изделия"
        verbose_name_plural = "Изделия"


class Workload(models.Model):
    ser = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Сотрудник", blank=True)
    load = models.CharField(max_length=150, verbose_name="Загруженность цеха")

    class Meta:
        verbose_name="Загруженность цеха"
        verbose_name_plural="Загруженность цеха"