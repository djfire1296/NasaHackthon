# -*- coding: utf-8 -*-

import geopy
from geopy.distance import VincentyDistance

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers




lat1 = 36.67
lon1 = 122.24


origin = geopy.Point(lat1, lon1)
destination = VincentyDistance(kilometers=100).destination(origin, 90)

lat2, lon2 = destination.latitude, destination.longitude

print lat2, lon2



"""
class GetAreaLatLon:
    def __init__(self, lat, lon, dist_x, dist_y):
        #要輸入 lat = 緯度, lon = 經度, dist_x = 水平距離, dist_y = 垂直距離
        if dist_x <= 0 or dist_y <= 0:
            raise ValueError(' Distance should be positive!')
        
        self.lat = lat
        self.lon = lon
        self.dist_x = dist_x
        self.dist_y = dist_y
    def vincentyDis(self, direction):
        origin = geopy.Point(self.lat, self.lon)
        if direction == 'up':
            b = 90
            d = self.dist_y
            destination = VincentyDistance(kilometers=d).destination(origin, b)
            lat2, lon2 = destination.latitude, destination.longitude
            return lat2, lon2
        
foo = GetAreaLatLon(lat1, lon1, 100, 100)

print foo.vincentyDis()
"""