from django.forms import BooleanField

NULLABLE = {'null': True, 'blank': True}


class StyleFormMixin:
    """Класс миксин стилизации формы"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"
