from events.models import Event
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView
from events.serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend
# import django_filters

# class EventFilter(django_filters.FilterSet):
#     startDate = django_filters.DateFilter(field_name="startDate")
#     endDate = django_filters.DateFilter(field_name="endDate")

#     class Meta:
#         model = Event
#         fields = 'startDate', 'endDate',

class EventAPIView(ListCreateAPIView):
    """
    API endpoint that allows events to be viewed or edited.
    """
    model = Event
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'startDate': ['gte'],
        'endDate': ['gte']
    }
    # filter_class = EventFilter
    # search_fields = ['id', 'title']
