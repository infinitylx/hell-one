# -*- coding: utf-8 -*-
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Catalog(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    visible = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    creating_date = models.DateTimeField('date published')
    modifying_date = models.DateTimeField('date modifyed')
    description = models.TextField()

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    creating_date = models.DateTimeField('date published')
    modifying_date = models.DateTimeField('date modifyed')
    parent = models.ForeignKey("self", related_name="children", blank=True, null=True)
    visible = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    #def delete(self):
    #    self.deleted = True

    def get_parents(self, children=[]):
        pars = []
        pars.append(children)

        if self.parent:
            print 'have parent'
            pars.insert(0, self.parent)
            print pars
            return pars
        print 'no parent'
        #print pars.insert(0, self)
        return pars

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
    visible = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    def delete(self):
        self.deleted = True

    def __unicode__(self):
        return self.name
