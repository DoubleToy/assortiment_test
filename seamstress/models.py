from django.db import models
from django.contrib.auth.models import User

CHOICE_OF_TYPE = (
    ('В', 'Выполнено'),
    ('Н', 'Не выполнено')
)


# Факт выполнения
class FactOfExecution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    completed = models.CharField(max_length=150, choices=CHOICE_OF_TYPE, verbose_name="Факт выполнения")
    spent = models.IntegerField(verbose_name="Затраченно времени")
    wages = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Зарплата", blank=True, null=True)

    class Meta:
        verbose_name = "Факт выполнения"
        verbose_name_plural = "Факт выполнения"


class Hours(models.Model):
    hours = models.IntegerField(verbose_name="Часы работы")
