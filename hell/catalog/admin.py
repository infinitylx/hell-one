# -*- coding: utf-8 -*-
from django.contrib import admin
from hell.catalog.models import Category, Attachment
from mptt.admin import MPTTModelAdmin

class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Attachment)