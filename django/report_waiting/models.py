# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class ReportWaiting(models.Model):
	waiting_lat = models.FloatField(max_length=20, default=-1.0)
	waiting_lon = models.FloatField(max_length=20, default=-1.0)
	waiting_num = models.CharField(max_length=20)
	remark_text = models.CharField(max_length=200, default=None)
	# response_lat = models.FloatField(max_length=20)
	# response_lon = models.FloatField(max_length=20)
	create_at = models.DateTimeField(auto_now_add=True)
	still_waiting = models.BooleanField(default=True)
