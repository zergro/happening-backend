from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'startDate', 'endDate')
    search_fields = ['title']

admin.site.register(Event, EventAdmin)