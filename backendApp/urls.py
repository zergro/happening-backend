from django.contrib import admin
from django.urls import path

from events import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/all', views.EventAPIView.as_view(), name='api'),
    path('api/future', views.FutureEventView.as_view(), name='api-future')
]