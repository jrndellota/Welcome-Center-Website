# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Members(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    wc_id = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Attendance(models.Model):

    member = models.ForeignKey(Members, on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.timestamp) + ': ' + self.memeber.__str__()
