from django.urls import path

from apps.main.apps import MainConfig
from apps.main.views import IndexView

app_name = MainConfig.name
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
