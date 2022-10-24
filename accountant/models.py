from django.db import models
from django.contrib.auth.models import User


# Тип работы
class TypeOfWork(models.Model):
    # Название работы
    name = models.CharField(max_length=100, db_index=True, verbose_name="Вид работы")
    # Стоймость в секундах
    cost = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Стоимость выполнения (в секундах)")

    class Meta:
        verbose_name = "Вид работы"
        verbose_name_plural = "Вид работы"


class Salary(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Сотрудник")
    wages = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Зарплата")

    class Meta:
        verbose_name = "Зарплата"
        verbose_name_plural = "Зарплата"
