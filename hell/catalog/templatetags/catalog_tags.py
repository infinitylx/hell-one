# -*- coding: utf-8 -*-
from django import template
from mptt.utils import *
from catalog.models import Category

register = template.Library()

@register.inclusion_tag('left-menu.html')
def left_menu(current_category=None):
    print "E V R I K A !"
    g = None
    res = []

    if current_category == None:
        res = Category.objects.root_nodes() # get root
    else:
        g = Category.objects.get(id=current_category)
        res = g.get_children()

    return {'node': g, 'others':res}
