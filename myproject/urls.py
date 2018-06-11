from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from strava import views



urlpatterns = [
    url('source/', views.source, name='source'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
