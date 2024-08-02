from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.client.forms import ClientForm
from apps.client.models import Client


class ClientListView(ListView):
    model = Client
    extra_context = {
        "title": "Список клиентов"
    }


class ClientDetailView(DetailView):
    model = Client
    extra_context = {
        "title": "Клиент сервиса"
    }


class ClientCreateView(CreateView):
    model = Client
    model_form = ClientForm
    extra_context = {
        "title": "Добавление клиента"
    }
    template_name = 'client/client_form.html'


class ClientUpdateView(UpdateView):
    model = Client
    model_form = ClientForm
    extra_context = {
        "title": "Редактирование клиента"
    }


class ClientDeleteView(DeleteView):
    model = Client
    extra_context = {
        "title": "Удаление клиента"
    }
