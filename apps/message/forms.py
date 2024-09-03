from django import forms
from apps.main.utils import StyleFormMixin
from apps.message.models import Message


class MessageForm(StyleFormMixin, forms.ModelForm):
    """Форма создания и редактирования сообщения"""

    class Meta:
        model = Message
        exclude = ("owner",)
