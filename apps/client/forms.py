from django import forms

from apps.client.models import Client
from apps.main.utils import StyleFormMixin


class ClientForm(StyleFormMixin, forms.ModelForm):
    """Форма создания и редактирования клиента"""

    class Meta:
        model = Client
        exclude = ("owner",)
