# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from hell.catalog.views import *

urlpatterns = patterns('',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<slug>\w+)/$', 'view_catalog', name='catalog'),
)