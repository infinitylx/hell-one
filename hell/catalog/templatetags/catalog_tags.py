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
    cats = Catalog.objects.all()
    par = Catalog.objects.get(id=current_category)
    ipars = drilldown_tree_for_node(par)

    return {'nodess':cats, 'par':par, 'pars':ipars}

    # Todo:
    # 0 get given object
    # 1 get path
    # 2 get all children from path
    # 3 get all from root level its useless coz all children from path already include those also.
