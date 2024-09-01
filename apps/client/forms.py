from django import forms

from apps.client.models import Client
from apps.main.utils import StyleFormMixin


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ("comment",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
