# -*- coding: utf-8 -*-

import geopy
from geopy.distance import VincentyDistance

# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers

(36.45994,-121.89938)


lat1 = 36.67
lon1 = 122.24


origin = geopy.Point(lat1, lon1)
destination = VincentyDistance(kilometers=100).destination(origin, 90)

lat2, lon2 = destination.latitude, destination.longitude

print lat2, lon2

https://maps.googleapis.com/maps/api/staticmap?key=YOUR_API_KEY&center=-33.751262851253905,150.58351745605464&
zoom=9&format=png&maptype=roadmap&
style=element:labels%7Cvisibility:off&
style=feature:administrative%7Celement:geometry%7Cvisibility:off&
style=feature:administrative.land_parcel%7Cvisibility:off&
style=feature:administrative.neighborhood%7Cvisibility:off&
style=feature:landscape.man_made%7Celement:geometry.fill%7Ccolor:0x808080&
style=feature:landscape.man_made%7Celement:geometry.stroke%7Cvisibility:off&
style=feature:poi%7Cvisibility:off&style=feature:road%7Celement:geometry.fill%7Ccolor:0x808080&
style=feature:road%7Celement:geometry.stroke%7Cvisibility:off&
style=feature:road%7Celement:labels.icon%7Cvisibility:off&
style=feature:transit%7Cvisibility:off&
style=feature:transit%7Celement:geometry.fill%7Ccolor:0x808080&
style=feature:transit%7Celement:geometry.stroke%7Cvisibility:off&
style=feature:water%7Celement:geometry.fill%7Ccolor:0x000000&

size=480x360