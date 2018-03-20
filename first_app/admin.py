# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from first_app import models
# Register your models here.

admin.site.register(models.Members)
admin.site.register(models.Attendance)
