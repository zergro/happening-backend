from events.models import Event
from rest_framework import generics
from rest_framework.generics import ListAPIView 
from events.serializers import EventSerializer
from django_filters import rest_framework as filters

class FutureEventView(ListAPIView):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.date.future().order_by('startDate')
    serializer_class = EventSerializer


class EventFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr='contains')
    startDate = filters.DateFilter(field_name="startDate", lookup_expr='gte')
    endDate = filters.DateFilter(field_name="startDate", lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['title', 'status', 'startDate', 'endDate']


class EventAPIView(generics.ListAPIView):
    """
    API endpoint that allows events to be viewed or edited.
    """
    queryset = Event.objects.all().order_by('startDate')
    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter
