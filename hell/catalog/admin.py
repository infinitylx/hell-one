# -*- coding: utf-8 -*-
from django.contrib import admin
from hell.catalog.models import Catalog, Category, Page, Attachment
from mptt.admin import MPTTModelAdmin

admin.site.register(Catalog, MPTTModelAdmin)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Attachment)