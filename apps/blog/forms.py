from django import forms
from apps.blog.models import Article
from apps.main.utils import StyleFormMixin


class ArticleForm(StyleFormMixin, forms.ModelForm):
    """Форма создания и редактирования статьи"""

    class Meta:
        model = Article
        exclude = (
            "slug",
            "count_views",
            "created_at",
            "owner",
        )
