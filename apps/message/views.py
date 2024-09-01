from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.message.forms import MessageForm
from apps.message.models import Message


class MessageListView(ListView):
    model = Message
    extra_context = {'title': 'Сообщения'}


class MessageDetailView(DetailView):
    model = Message
    extra_context = {'title': 'Информация о сообщении'}


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    extra_context = {'title': 'Создание сообщения'}
    success_url = reverse_lazy('messages:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    extra_context = {'title': 'Редактирование сообщения'}

    def get_success_url(self):
        return reverse('messages:message_detail', args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    model = Message
    extra_context = {'title': 'Удаление сообщения'}
    success_url = reverse_lazy('messages:message_list')
