from django.conf.urls import patterns, include, url

from .views import inicio

urlpatterns = [
     url(r'^$', inicio.as_view(), name='index'),
]
