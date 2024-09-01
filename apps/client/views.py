from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from apps.client.forms import ClientForm
from apps.client.models import Client


class ClientListView(ListView):
    model = Client
    extra_context = {"title": "Клиенты сервиса"}


class ClientDetailView(DetailView):
    model = Client
    extra_context = {"title": "Информация о клиенте"}


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    extra_context = {"title": "Добавление клиента"}
    success_url = reverse_lazy("clients:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    extra_context = {"title": "Редактирование клиента"}

    def get_success_url(self):
        return reverse("clients:client_detail", args=[self.kwargs.get("pk")])


class ClientDeleteView(DeleteView):
    model = Client
    extra_context = {"title": "Удаление клиента"}
    success_url = reverse_lazy("clients:client_list")
