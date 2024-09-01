from django.core.management import BaseCommand
from apps.mailing.services import run_mailing


class Command(BaseCommand):
    def handle(self, *args, **options):
        run_mailing()
