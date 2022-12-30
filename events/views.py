from events.models import Event
from rest_framework import generics
from rest_framework.generics import ListAPIView 
from events.serializers import EventSerializer

class EventAPIView(generics.ListAPIView):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('startDate')
    serializer_class = EventSerializer
