# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from first_app.models import Attendance
# Create your views here.

def index(request):
    return render(request, 'index.html',)
