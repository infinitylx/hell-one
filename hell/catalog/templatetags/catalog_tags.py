# -*- coding: utf-8 -*-
from django import template
from mptt.utils import *
from catalog.models import Category

register = template.Library()

@register.inclusion_tag('left-menu.html')
def left_menu(current_category=None):
    #print "E V R I K A !"

    if current_category == None:
        g = Category.objects.root_nodes()[0] # get root
    else:
        g = Category.objects.get(id=current_category)

    ipath = drilldown_tree_for_node(g)
    path = []
    others = {}

    for p in ipath:
        path.append(p)

    res = rec_call(path, path[0])

    return {'node':g, 'path':path, 'others':res}

def rec_call(path, parent):
    """ 0 close list
    1 open list
    2 do nothing
    """

    res = []
    b = False
    for p in parent.get_children():
        if p in path:
            res.append([p, 1])
            r = rec_call(path, p)
            b = True
            if len(r) == 1:
                res.extend([r])
            else:
                res.extend(r)
        else:
            if b:
                res.append([p, 0])
            else:
                res.append([p, 2])
            b = False

    return res