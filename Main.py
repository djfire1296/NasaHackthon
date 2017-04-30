import AreaZoneCal as azl
import wind 
import get_googlemap

lat = 36.45994
lon = -121.89938

g = area.GetAreaLatLon(lat, lon) # use default distance 20, 20, 10, 10 (left, right, up, down)

upleft, downright = g.vincentyDis()

get_googlemap.get_map(upleft, downright)

w = wind(lat, lon)

winddata = w.get_weatherdata()

print winddata['speed']
print winddata['deg']