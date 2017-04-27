#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 18:26:36 2017

@author: moon
"""

from cStringIO import StringIO
from PIL import Image
import urllib
import matplotlib as plt



url = "http://maps.googleapis.com/maps/api/staticmap?center=-30.027489,-51.229248&size=800x800&zoom=14&sensor=false"
buffer = StringIO(urllib.urlopen(url).read())
imageTest = Image.open(buffer)



imageTest.show()
#plt.show()