import random
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.forms import BooleanField
from apps.blog.models import Article

NULLABLE = {'blank': True, 'null': True}


class StyleFormMixin:
    """Класс миксин стилизации формы"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fields_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class AccessCheckMixin:
    """Класс миксин проверки на суперюзера и создателя объекта"""

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if not user.is_superuser and user != self.object.owner:
            raise PermissionDenied
        return self.object


def get_random_articles(count: int) -> list:
    queryset_count = Article.objects.aggregate(count=Count('id'))['count']

    if queryset_count == 0:
        random_articles = []
    elif count >= queryset_count:
        random_articles = list(Article.objects.all())
    else:
        random_indexes = random.sample(range(queryset_count), count)
        random_articles = [Article.objects.all()[index] for index in random_indexes]
    return random_articles
