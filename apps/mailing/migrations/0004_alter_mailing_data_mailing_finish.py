# Generated by Django 5.0.7 on 2024-09-03 03:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0003_alter_mailing_data_mailing_finish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="data_mailing_finish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2025, 9, 3, 3, 25, 37, 428840, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Дата завершения",
            ),
        ),
    ]