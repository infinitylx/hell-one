# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from catalog.models import Category

def index(request):
    return render_to_response('index.html')

def view_catalog(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('category.html', {'category':category})