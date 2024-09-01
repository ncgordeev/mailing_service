from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from apps.message.forms import MessageForm
from apps.message.models import Message


class MessageListView(ListView):
    model = Message
    extra_context = {"title": "Сообщения"}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class MessageDetailView(DetailView):
    model = Message
    extra_context = {"title": "Информация о сообщении"}


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    extra_context = {"title": "Создание сообщения"}
    success_url = reverse_lazy("messages:message_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    extra_context = {"title": "Редактирование сообщения"}

    def get_success_url(self):
        return reverse("messages:message_detail", args=[self.kwargs.get("pk")])


class MessageDeleteView(DeleteView):
    model = Message
    extra_context = {"title": "Удаление сообщения"}
    success_url = reverse_lazy("messages:message_list")
