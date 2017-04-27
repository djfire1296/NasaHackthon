#!/usr/bin/python
# -*- coding: utf-8 -*-
from api_key import * #不要讓 api 的 key 直接上傳 github
import pyowm

#print API

owm = pyowm.OWM(API)  #要換掉 API 如果你沒有這個檔
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()

print (w.get_wind())
print (w.get_humidity())
print (w.get_temperature('celsius'))
