from django.contrib.auth.models import AbstractUser
from django.db import models

from main.utils import NULLABLE


class User(AbstractUser):
    """Модель пользователя."""
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    surname = models.CharField(max_length=50, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(max_length=150, verbose_name='Электронная почта')
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Аватар', **NULLABLE)
    token = models.CharField(max_length=255, verbose_name='Токен')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
