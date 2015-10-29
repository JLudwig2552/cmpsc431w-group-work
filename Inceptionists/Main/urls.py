__author__ = 'Frank'

from django.conf.urls import patterns, url
from Main import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
