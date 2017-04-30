# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime as ddt
from PIL import Image
import urllib, StringIO

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.conf import settings

from .models import ReportWaiting
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def report_waiting(request):
	waiting_lat = request.GET.get('waiting_lat', '')
	waiting_lon = request.GET.get('waiting_lon', '')
	waiting_num = request.GET.get('inlineRadioOptions', '')

	if waiting_lat != '' and waiting_lon != '' and waiting_num != '':
		new_WaitingData = ReportWaiting()
		new_WaitingData.waiting_lat = float(waiting_lat)
		new_WaitingData.waiting_lon = float(waiting_lon)

		if waiting_num == 'option1':
			new_WaitingData.waiting_num = '2'
		elif waiting_num == 'option2':
			new_WaitingData.waiting_num = '5'
		elif waiting_num == 'option3':
			new_WaitingData.waiting_num = '8'
		else:
			new_WaitingData.waiting_num = '12'

		new_WaitingData.remark_text = request.GET.get('remark', '')
		new_WaitingData.create_at = ddt.utcnow()
		new_WaitingData.still_waiting = True

		new_WaitingData.save()
		return HttpResponseRedirect('/report_waiting')

	num = ReportWaiting.objects.count()
	if num < 10:
		waiting_list = ReportWaiting.objects.all().reverse()[:num]
	else:
		waiting_list = ReportWaiting.objects.all().reverse()[:10]

	still_wait_list = list(ReportWaiting.objects.filter(still_waiting=True))
	response = HttpResponse()

	return render(request, 'report_waiting.html', {
		'GOOGLE_MAP_API_KEY': settings.GOOGLE_MAP_API_KEY,
		'waiting_list': waiting_list
		})

def report_place(request):
	return render(request, 'report_place.html', {})

def report_upload(request):
	return render(request, 'report_upload.html', {})

def soledad_fire(request):
	return render(request, 'soledad_fire.html', {})