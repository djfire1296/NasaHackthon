import AreaZoneCal as azl
import wind 
import get_googlemap

# lat = 36.45994
# lon = -121.89938
lat = 25.022049
lon = 121.535504

g = azl.GetAreaLatLon(lat, lon) # use default distance 20, 20, 10, 10 (left, right, up, down)

upleft, downright = g.vincentyDis()

get_googlemap.get_map(upleft, downright)

w = wind.GetWeatherData(lat, lon)

winddata = w.get_weatherdata()

print winddata['speed']
print winddata['deg']