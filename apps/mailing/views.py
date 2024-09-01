from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from apps.mailing.forms import MailingForm
from apps.mailing.models import Mailing


class MailingListView(ListView):
    model = Mailing
    extra_context = {"title": "Рассылки"}


class MailingDetailView(DetailView):
    model = Mailing
    extra_context = {"title": "Информация о рассылке"}


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {"title": "Создание рассылки"}
    success_url = reverse_lazy("mailings:mailing_list")

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
