# -*- coding: utf-8 -*-
from django import template
#from django.conf import settings
#from django.template.defaultfilters import stringfilter
from mptt.utils import *

from catalog.models import Category, Catalog

#import datetime

register = template.Library()

@register.inclusion_tag('left-menu.html')
def left_menu(current_category=7):
    print "E V R I K A !"
    #cats = Catalog.objects.all()
    g = Catalog.objects.get(id=current_category)
    ipath = drilldown_tree_for_node(g)
    path = []
    others = {}
    allcats = []

    for p in ipath:
        path.append(p)

    # some part of next two cicles need to be moved to recursive function. but what part exactly???
    res = rec_call(path, path[0])
    print g
    print res

    return {'node':g, 'path':path, 'others':others}

    # Todo:
    # 0 get given object
    # 1 get path
    # 2 get all children from path
    # 3 get all from root level its useless coz all children from path already include those also.

def rec_call(path, parent):
    res = []
    for p in parent.get_children():
        res.append(p)
        if p in path:
            res.extend(rec_call(path, p))
    return res