from django import forms

from apps.mailing.models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
