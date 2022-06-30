from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Organizer)
admin.site.register(Event)