# -*- coding: utf-8 -*-

import reverse_geocoder as rg

coordinates = (36.45994,-121.89938)

results = rg.search(coordinates, mode=1) # default mode = 2

print results[0]['admin2']

