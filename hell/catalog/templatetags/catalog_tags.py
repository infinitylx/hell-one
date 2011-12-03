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
    res = rec_call(path, path[0], 0)
    print g
    print res

    return {'node':g, 'path':path, 'others':res[0]}

def rec_call(path, parent, counts):
    """ 0 close list
    1 open list
    2 nothing
    """
    res = []
    b = False
    for p in parent.get_children():


        if p in path:
            res.append([p, 1])
            counts += 1
            r = rec_call(path, p, counts)
            b = True
            if len(r[0]) == 1:
                res.extend([r[0]])
            else:
                res.extend(r[0])
        else:
            if b:
                res.append([p, 0])
            else:
                res.append([p, 2])
            b = False

    #if len(res) == 0:
    #    res = [None, 0]

    return (res, counts-1)