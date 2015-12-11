__author__ = 'Frank'

from django.conf.urls import patterns, url
from Main import views

urlpatterns = patterns('',
        url(r'^Main/category/(?P<category_name>\w+)/$', views.category, name='category'),
        url(r'^$', views.index, name='index'),
        url(r'^$', views.about, name='about'),
        url(r'^add_user/$', views.add_user, name='add_user'),
                       #r'^stores/(?P<store_id>\d+)/'
        #url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)
        )