from django import forms

from apps.client.models import Client
from apps.main.utils import StyleFormMixin


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('comment',)
