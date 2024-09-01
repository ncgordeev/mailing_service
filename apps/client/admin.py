from django.contrib import admin

from apps.client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
    )
    search_fields = (
        "first_name",
        "email",
    )
    list_filter = (
        "id",
        "first_name",
        "email",
    )
