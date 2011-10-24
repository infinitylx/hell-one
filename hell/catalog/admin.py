# -*- coding: utf-8 -*-
from django.contrib import admin
from hell.catalog.models import Category, Page, Attachment

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Attachment)