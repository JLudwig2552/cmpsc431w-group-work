"""Inceptionists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin

#urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
#]

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^Main/category/.','Main.views.category'),
    #url(r'^Main/category/.',include('Main.urls')),
    url(r'^Main/category/(?P<category_name>\w+)$','Main.views.category'),
    url(r'^Main/about/','Main.views.about'),
    url(r'^Main/', 'Main.views.index'),

    #url(r'^Main/', include('Main.urls')), # ADD THIS NEW TUPLE!
)
