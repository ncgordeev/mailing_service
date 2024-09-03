from django.contrib import admin

from apps.client.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "surname",
        "email",
    )
    list_filter = ("owner",)
    search_fields = ("email",)
