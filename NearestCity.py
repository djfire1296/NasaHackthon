# -*- coding: utf-8 -*-

import reverse_geocoder as rg

def find_neareastCity(lat, lon):

	results = rg.search((lat, lon), mode=2) # default mode = 2
	print results

	return results[0]

