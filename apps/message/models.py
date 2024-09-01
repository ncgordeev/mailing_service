from django.db import models

from config import settings


class Message(models.Model):
    """Модель сообщения в рассылке"""

    letter_body = models.TextField(verbose_name="Тело письма")
    letter_subject = models.CharField(max_length=150, verbose_name="Тема письма")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель"
    )

    def __str__(self):
        return self.letter_subject

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
