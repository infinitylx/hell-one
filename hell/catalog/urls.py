# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from hell.catalog.views import *

urlpatterns = patterns('',
    url(r'/(?P<slug>\w+)', 'hell.catalog.views.view_catalog', name='catalog'),
    url(r'/$', 'hell.catalog.views.index', name='index'),
)