from django.urls import path

from apps.blog.apps import BlogConfig
from apps.blog.views import (
    ArticleListView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("view/<slug:slug>", ArticleDetailView.as_view(), name="article_view"),
    path("update/<int:pk>", ArticleUpdateView.as_view(), name="article_update"),
    path("delete/<int:pk>", ArticleDeleteView.as_view(), name="article_delete"),
]
