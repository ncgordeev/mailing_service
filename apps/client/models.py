from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from apps.main.utils import NULLABLE


class Client(models.Model):
    """Модель клиент сервиса, получает рассылки"""

    first_name = models.CharField(max_length=50, verbose_name="Имя", default=None)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", default=None)
    surname = models.CharField(max_length=50, verbose_name="Отчество")
    email = models.EmailField(max_length=256, verbose_name="Почта")
    comment = models.TextField(max_length=450, **NULLABLE, verbose_name="Комментарий")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}".title()

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        unique_together = ["email", "owner"]
