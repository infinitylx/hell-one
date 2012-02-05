# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify
from smart_slug.fields import SmartSlugField
from datetime import datetime
import os
# for custom smart-slug-field
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^smart_slug\.fields\.SmartSlugField"]) # add south rule for custom field

def upload_path_handler(instance, filename):
    """Upload files under 'category/subcategory/.../' """
    path = []
    
    for p in instance.category.get_ancestors(ascending=False): # getting all parents category
        path.append(p.slug)
    
    path = "/".join(path) # rendering it to string
    ext = os.path.splitext(filename)[1] # getting extension from original file
    file_name = "%Y-%m-%d_%H:%M" + ext # set filename as date plus original extension, prepare template
    path += datetime.today().strftime(file_name) # set actual date
    return "Catalog/{category}/".format(category=path)

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = SmartSlugField(
        source_field='name',
        #date_field='creating_date', #coz no date before saving # BUG
        split_on_words=True,
        underscores=False,
        max_length=50)
    description = models.TextField(blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    visible = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    creating_date = models.DateTimeField('date published', auto_now=True, auto_now_add=False)
    modifying_date = models.DateTimeField('date modifyed', auto_now=False, auto_now_add=True)
    #attachment = models.ManyToManyField(Attachment, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name

    #@models.permalink
    def get_absolute_url(self):
        """Construct the absolute URL for this Item."""
        return reverse("hell.catalog.views.view_catalog", args=[self.slug])

    # no need for this coz it's all done in smartslug. I hope :-)
    # def save(self, *args, **kwargs):

    #     if not self.id:
    #        self.slug = slugify(self.name)

    #     super(Category, self).save(*args, **kwargs)

class Attachment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    document = models.FileField(upload_to=upload_path_handler)
    category = models.ForeignKey('Category')

    def __unicode__(self):
        return self.name
