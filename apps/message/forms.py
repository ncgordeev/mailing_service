from django import forms

from apps.message.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
