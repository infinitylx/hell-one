# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    creating_date = models.DateTimeField('date published')
    modifying_date = models.DateTimeField('date modifyed')
    sub_categoryes = models.ManyToManyField("self", blank=True, null=True)

    def __unicode__(self):
        return self.name

class Attachment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    document = models.FileField(upload_to="attachments")

    def __unicode__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField()
    attachment = models.ManyToManyField(Attachment, blank=True, null=True)
    creating_date = models.DateTimeField('date published')
    modifying_date = models.DateTimeField('date modifyed')

    def __unicode__(self):
        return self.name
