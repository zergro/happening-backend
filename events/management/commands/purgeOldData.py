from django.core.management.base import BaseCommand

from events.models import Event
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = 'Delete objects older than 1 day'
    def handle(self, *args, **options):
        try:
            counter = 0
            deleteList = Event.objects.filter(endDate__lte=datetime.now()-timedelta(days=1))
            for i in deleteList:
                counter = counter + 1
            print('Length of delete list is: '+ str(counter))
            deleteList.delete()
        except:
            print('Something happened')
        self.stdout.write('job complete')