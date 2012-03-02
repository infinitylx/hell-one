# -*- coding: utf-8 -*-
from django.contrib import admin
from hell.catalog.models import Category, Attachment
from mptt.admin import MPTTModelAdmin

# class CategoryAdmin(MPTTModelAdmin):
#     prepopulated_fields = {'slug': ('name',)}

class AttachmentInline(admin.StackedInline):
    model = Attachment
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    inlines = [AttachmentInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Attachment)