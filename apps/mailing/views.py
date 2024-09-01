from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from apps.client.models import Client
from apps.mailing.forms import MailingForm
from apps.mailing.models import Mailing, Logs


class MailingListView(ListView):
    model = Mailing
    extra_context = {"title": "Рассылки"}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MailingDetailView(DetailView):
    model = Mailing
    extra_context = {"title": "Информация о рассылке"}


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {"title": "Создание рассылки"}
    success_url = reverse_lazy("mailings:mailing_list")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['client_mailing'].queryset = Client.objects.filter(owner=self.request.user)
        return form

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {"title": "Редактирование рассылки"}

    def get_success_url(self):
        return reverse("mailings:mailing_detail", args=[self.kwargs.get("pk")])


class MailingDeleteView(DeleteView):
    model = Mailing
    extra_context = {"title": "Удаление рассылки"}
    success_url = reverse_lazy("mailings:mailing_list")


class LogListView(ListView):
    model = Logs
    extra_context = {'title': 'Лог рассылок'}

    def get_queryset(self, *args, **kwargs):
        mailing_pk = self.kwargs.get('mailing_pk')
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(mailing__pk=mailing_pk)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['mailing_pk'] = self.kwargs.get('mailing_pk')
        return context
