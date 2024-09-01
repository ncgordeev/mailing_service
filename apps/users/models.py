from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name="Email")
    first_name = models.CharField(max_length=50, verbose_name="Имя", **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)
    country = models.CharField(max_length=100, verbose_name="Страна", **NULLABLE)
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", **NULLABLE
    )
    token = models.CharField(max_length=120, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
