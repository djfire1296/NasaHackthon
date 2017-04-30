#!/usr/bin/python
# -*- coding: utf-8 -*-
from api_key import * #不要讓 api 的 key 直接上傳 github
import pyowm
import reverse_geocoder as rg

class GetWeatherData():

	def __init__(self, lat, lon):
		self.lat = lat
		self.lon = lon
		self.owm = pyowm.OWM(API)


	def find_neareastCity(self):
		results = rg.search((self.lat, self.lon), mode=1) # default mode = 2
		return results[0] # only return first result

	# 36.3367668574,-121.706133118 Soberane
	# 24.45994,121.89938 Taiwan
	def get_weatherdata(self):
		# Get the nearest station
		try:
			nearest_station = self.owm.station_at_coords(self.lat, self.lon)
			ns_observation = nearest_station[0].get_last_weather()
			wind_observation = ns_observation.get_wind()
			print wind_observation
			return wind_observation

		except KeyError:

			print "Can't find station near the location, use the nearest city instead..."
			nearest_city = find_neareastCity(self.lat, self.lon)
			nearest_city_station = self.owm.weather_at_place(nearest_city['admin2'])
			ncs_observation = nearest_city_station.get_weather()
			wind_observation = ncs_observation.get_wind()
			print wind_observation
			return wind_observation

if __name__ == '__main__':
	get_weatherdata(36.3367668574,-121.706133118)
	get_weatherdata(24.45994,121.89938)
