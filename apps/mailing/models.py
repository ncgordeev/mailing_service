from django.conf import settings
from django.db import models

from apps.client.models import Client
from apps.message.models import Message

from apps.main.utils import NULLABLE


class Mailing(models.Model):
    """Модель рассылки"""

    PERIODICITY_MAILING = [
        ("once_day", "раз в день"),
        ("once_week", "раз в неделю"),
        ("once_month", "раз в месяц"),
    ]

    STATUS_MAILING = [
        ("created", "создана"),
        ("launched", "запущена"),
        ("completed", "завершена"),
    ]

    name = models.CharField(max_length=50, verbose_name="Название")
    data_mailing = models.DateTimeField(verbose_name="Начало")
    data_mailing_finish = models.DateTimeField(**NULLABLE, verbose_name="Завершение")
    periodicity = models.CharField(
        max_length=10, choices=PERIODICITY_MAILING, verbose_name="Периодичность"
    )
    client_mailing = models.ManyToManyField(Client, verbose_name="Получатель")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель"
    )
    status = models.CharField(
        max_length=9, choices=STATUS_MAILING, verbose_name="Статус"
    )
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение', default=None)

    def __str__(self):
        return f"Рассылка: {self.name}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
