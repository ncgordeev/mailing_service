# Generated by Django 5.0.7 on 2024-09-01 11:57

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0002_client_owner"),
        ("mailing", "0003_alter_mailing_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="sent_time",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата отправки"
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="client_mailing",
            field=models.ManyToManyField(to="client.client", verbose_name="Получатели"),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="data_mailing",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата создания"
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="data_mailing_finish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 9, 1, 11, 57, 4, 781126, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата завершения",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="periodicity",
            field=models.CharField(
                choices=[
                    ("Один раз", "Один раз"),
                    ("Ежедневно", "Ежедневно"),
                    ("Еженедельно", "Еженедельно"),
                    ("Ежемесячно", "Ежемесячно"),
                ],
                default="Один раз",
                verbose_name="Периодичность",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("Создана", "Создана"),
                    ("Запущена", "Запущена"),
                    ("Завершена", "Завершена"),
                ],
                default="Создана",
                verbose_name="Статус",
            ),
        ),
        migrations.CreateModel(
            name="Logs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("datatime", models.DateTimeField(verbose_name="Дата и время попытки")),
                (
                    "status",
                    models.CharField(
                        choices=[("Успешно", "Успешно"), ("Безуспешно", "Безуспешно")],
                        verbose_name="Статус",
                    ),
                ),
                (
                    "answer_mail_server",
                    models.TextField(verbose_name="Ответ почтового сервера"),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка",
                "verbose_name_plural": "Попытки",
            },
        ),
    ]