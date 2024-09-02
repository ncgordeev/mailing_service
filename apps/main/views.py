from django.views.generic import TemplateView

from apps.blog.models import Article
from apps.client.models import Client
from apps.mailing.models import Mailing
from apps.main.utils import get_random_articles


class IndexView(TemplateView):
    extra_context = {'title': 'Главная'}
    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        mailing = Mailing.objects.all()
        clients = Client.objects.all()
        context['count_mailing'] = mailing.count()
        context['count_mailing_active'] = mailing.filter(status=Mailing.StatusOfMailing.LAUNCHED).count()
        context['articles_random'] = Article.objects.all()
        context['count_client'] = clients.count()
        context['count_client_unique'] = clients.values('email').distinct().count()
        context['object_list'] = get_random_articles(3)
        return context
