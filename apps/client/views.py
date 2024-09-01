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

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class ClientDetailView(DetailView):
    model = Client
    extra_context = {"title": "Информация о клиенте"}


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    extra_context = {"title": "Добавление клиента"}
    success_url = reverse_lazy("clients:client_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


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
