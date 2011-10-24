# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

from catalog.models import Category

import datetime

register = template.Library()

@register.inclusion_tag('left-menu.html')
def left_menu(curent_category=None):
    categories = Category.objects.filter(hide=False)
    return {'categories':categories, 'curent_category':curent_category, }
