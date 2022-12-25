from django.core.management.base import BaseCommand

from events.models import Event
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Delete objects older than 1 day'
    def handle(self, *args, **options):
        Event.objects.filter(endDate__lte=datetime.now()-timedelta(days=1)).delete()
        self.stdout.write('job complete')




