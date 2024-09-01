from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.main.utils import NULLABLE


class User(AbstractUser):
    """Модель пользователя."""

    username = None

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    surname = models.CharField(max_length=50, verbose_name="Отчество", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)
    email = models.EmailField(
        max_length=150, unique=True, verbose_name="Электронная почта"
    )
    avatar = models.ImageField(upload_to="avatars/", verbose_name="Аватар", **NULLABLE)
    token = models.CharField(max_length=255, verbose_name="Токен")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        permissions = [
            ("set_user_deactivate", "Can user deactivate"),
            ("view_all_users", "Can view all users"),
        ]
