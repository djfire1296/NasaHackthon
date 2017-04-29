# -*- coding: utf-8 -*-

from PIL import Image
import urllib, StringIO
from math import log, exp, tan, atan, pi, ceil
import geopy
from geopy.distance import VincentyDistance
#一定要裝 geopy

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers
# bearing 是方位, 這是0~360, 所以我們要找的在 0, 90, 180, 270, 360

class GetAreaLatLon:

    def __init__(self, lat, lon, dist_left_x, dist_right_x, dist_down_y, dist_up_y):
        #要輸入 lat = 緯度, lon = 經度, dist_x = 水平距離, dist_y = 垂直距離
        if dist_left_x <= 0 or dist_right_x <= 0 or dist_up_y < 0 or dist_down_y < 0 :
            raise ValueError(' Distance should be positive!')
        
        self.lat = lat
        self.lon = lon
        self.dist_left_x = dist_left_x
        self.dist_right_x = dist_right_x
        self.dist_up_y = dist_up_y
        self.dist_down_y = dist_down_y
        
    def vincentyDis(self):
        origin = geopy.Point(self.lat, self.lon)
        
        # left 
        left_destination = VincentyDistance(kilometers=self.dist_left_x) \
                                    .destination(origin, 270)
                                    
        # up
        up_destination = VincentyDistance(kilometers=self.dist_up_y) \
                                    .destination(origin, 0)
        
        # right
        right_destination = VincentyDistance(kilometers=self.dist_right_x) \
                                    .destination(origin, 90)  
                                    
        # down
        down_destination = VincentyDistance(kilometers=self.dist_down_y) \
                                    .destination(origin, 180)
                                    
                                    
        left_lon = left_destination.longitude
        up_lat = up_destination.latitude
        
        right_lon = right_destination.longitude
        down_lat = down_destination.latitude
        
        upleft = ','.join((str(up_lat), str(left_lon)))
        downright = ','.join((str(down_lat), str(right_lon)))
        
        return upleft, downright
