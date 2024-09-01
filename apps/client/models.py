from django.db import models

from apps.main.utils import NULLABLE


class Client(models.Model):
    """Класс модели для клиентов"""

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    surname = models.CharField(max_length=50, verbose_name="Отчество", **NULLABLE)
    email = models.EmailField(max_length=150, verbose_name="Электронная почта")
    comment = models.TextField(verbose_name="Комментарий", **NULLABLE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.surname}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
