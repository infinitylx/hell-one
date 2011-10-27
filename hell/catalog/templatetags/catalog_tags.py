# -*- coding: utf-8 -*-
from django import template
#from django.conf import settings
#from django.template.defaultfilters import stringfilter

from catalog.models import Category

#import datetime

register = template.Library()

@register.inclusion_tag('left-menu.html')
def left_menu(current_category=None):
    categories = Category.objects.filter(visible=True)
    cats = []
    cats.extend(categories)

    if current_category != None:
        print current_category
        sel_cat = Category.objects.get(id=current_category)

        if sel_cat != None:
            parents = sel_cat.get_parents()
            print 'parents'
            print parents

            if parents != None:
                for cat in cats:
                    if parents[0].id == cat.id:
                        cats[cats.index(cat)] = parents
                        print "E v r i k a !"
                        print cats


    return {'categories':cats, 'current_category':current_category, }
