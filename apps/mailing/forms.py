from django import forms

from apps.mailing.models import Mailing
from apps.main.utils import StyleFormMixin


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Форма создания и редактирования рассылки"""

    class Meta:
        model = Mailing
        exclude = (
            "data_mailing",
            "owner",
        )


class ManagerMailingForm(StyleFormMixin, forms.ModelForm):
    """Форма редактирования рассылки для менеджера"""

    class Meta:
        model = Mailing
        fields = ("status",)
