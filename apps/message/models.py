from django.conf import settings
from django.db import models

from apps.main.utils import NULLABLE


class Message(models.Model):
    """Модель сообщение в рассылке"""
    letter_subject = models.CharField(max_length=150, verbose_name='Тема письма')
    letter_body = models.TextField(verbose_name='Тело письма')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)

    def __str__(self):
        return f"{self.letter_subject}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
