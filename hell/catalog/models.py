# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.template.defaultfilters import slugify

class Attachment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    document = models.FileField(upload_to="attachments")

    def __unicode__(self):
        return self.name

class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    visible = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    creating_date = models.DateTimeField('date published')
    modifying_date = models.DateTimeField('date modifyed')
    attachment = models.ManyToManyField(Attachment, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name

    #@models.permalink
    def get_absolute_url(self):
        """Construct the absolute URL for this Item."""
        return reverse("hell.catalog.views.view_catalog", args=['odin'])

    def save(self, *args, **kwargs):

        if not self.id:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

