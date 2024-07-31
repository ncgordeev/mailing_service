from django.urls import path

from main.views import IndexView
from main.apps import MainConfig

app_name = MainConfig.name
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
