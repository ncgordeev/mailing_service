from django.db import models


class Message(models.Model):
    letter_subject = models.CharField(max_length=150, verbose_name='Тема письма')
    letter_body = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.letter_subject}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
