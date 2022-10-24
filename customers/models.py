from django.db import models
from django.contrib.auth.models import AbstractUser


class Settings(models.Model):
    # Стоймость одной секунды
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройки"

