from django.contrib import admin

from apps.message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "letter_subject",
    )
    list_filter = ("owner",)
    search_fields = ("letter_subject",)
