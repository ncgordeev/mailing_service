from django import forms
from django.core.exceptions import ValidationError
from apps.client.models import Client
from apps.main.utils import StyleFormMixin


class ClientForm(StyleFormMixin, forms.ModelForm):
    """Форма создания и редактирования клиента"""

    class Meta:
        model = Client
        exclude = ("owner",)

    def __init__(self, *args, owner, **kwargs):
        self.owner = owner
        super().__init__(*args, **kwargs)

    def clean_blog_image(self):
        """Clean метод добавляющий по дефолту картинку"""
        blog_image = self.cleaned_data.get("blog_image")
        if not blog_image:
            blog_image = "article_example.jpg"
        return blog_image

    def clean_email(self):
        """Clean метод проверяющий уникальность email клиента
        среди клиентов пользователя"""
        email = self.cleaned_data.get("email")
        if Client.objects.filter(email=email, owner=self.owner).exists():
            raise ValidationError("Повторяющийся email!")
        return email
