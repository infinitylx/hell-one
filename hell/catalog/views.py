# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    con = "Hello, world. You're at the poll index."
    return render_to_response('index.html', {'con':con})