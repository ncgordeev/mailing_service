from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from apps.message.forms import MessageForm
from apps.message.models import Message


class MessageListView(ListView):
    model = Message
    extra_context = {"title": "Сообщения"}


class MessageDetailView(DetailView):
    model = Message
    extra_context = {"title": "Сообщение"}


class MessageCreateView(CreateView):
    model = Message
    model_form = MessageForm
    fields = ["letter_body", "letter_subject"]
    extra_context = {"title": "Создание сообщения"}
    success_url = reverse_lazy("messages:message_list")


class MessageDeleteView(DeleteView):
    model = Message
    model_form = MessageForm
    extra_context = {"title": "Удаление сообщения"}
    success_url = reverse_lazy("messages:message_list")


class MessageUpdateView(UpdateView):
    model = Message
    extra_context = {"title": "Редактирование сообщения"}
    success_url = reverse_lazy("messages:message_list")
