# Generated by Django 5.0.7 on 2024-09-03 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="avatars",
            new_name="avatar",
        ),
    ]
