from PIL import Image
import urllib, StringIO
from math import log, exp, tan, atan, pi, ceil
from googlemap_api_key import *

EARTH_RADIUS = 6378137
EQUATOR_CIRCUMFERENCE = 2 * pi * EARTH_RADIUS
INITIAL_RESOLUTION = EQUATOR_CIRCUMFERENCE / 256.0
ORIGIN_SHIFT = EQUATOR_CIRCUMFERENCE / 2.0

def latlontopixels(lat, lon, zoom):
    mx = (lon * ORIGIN_SHIFT) / 180.0
    my = log(tan((90 + lat) * pi/360.0))/(pi/180.0)
    my = (my * ORIGIN_SHIFT) / 180.0
    res = INITIAL_RESOLUTION / (2**zoom)
    px = (mx + ORIGIN_SHIFT) / res
    py = (my + ORIGIN_SHIFT) / res
    return px, py

def pixelstolatlon(px, py, zoom):
    res = INITIAL_RESOLUTION / (2**zoom)
    mx = px * res - ORIGIN_SHIFT
    my = py * res - ORIGIN_SHIFT
    lat = (my / ORIGIN_SHIFT) * 180.0
    lat = 180 / pi * (2*atan(exp(lat*pi/180.0)) - pi/2.0)
    lon = (mx / ORIGIN_SHIFT) * 180.0
    return lat, lon

    ############################################

    # a neighbourhood in Lajeado, Brazil:

    # upperleft =  '-29.44,-52.0'  
    # lowerright = '-29.45,-51.98'

    ############################################

def get_map(upperleft='36.67,-122.24', lowerright='36.29,-121.60', zoom = 12):
    ullat, ullon = map(float, upperleft.split(','))
    lrlat, lrlon = map(float, lowerright.split(','))

    # Set some important parameters
    scale = 1
    maxsize = 640

    # convert all these coordinates to pixels
    ulx, uly = latlontopixels(ullat, ullon, zoom)
    lrx, lry = latlontopixels(lrlat, lrlon, zoom)

    # calculate total pixel dimensions of final image
    dx, dy = lrx - ulx, uly - lry

    # calculate rows and columns
    cols, rows = int(ceil(dx/maxsize)), int(ceil(dy/maxsize))

    # calculate pixel dimensions of each small image
    bottom = 120
    largura = int(ceil(dx/cols))
    altura = int(ceil(dy/rows))
    alturaplus = altura + bottom


    satellite_final = Image.new("RGB", (int(dx), int(dy)))
    road_final = Image.new("RGB", (int(dx), int(dy)))

    for x in range(cols):
        for y in range(rows):
            dxn = largura * (0.5 + x)
            dyn = altura * (0.5 + y)
            latn, lonn = pixelstolatlon(ulx + dxn, uly - dyn - bottom/2, zoom)
            position = ','.join((str(latn), str(lonn)))
            print x, y, position, largura, alturaplus
            surlparams = urllib.urlencode({'center': position,
                                           'zoom': str(zoom),
                                           'size': '%dx%d' % (largura, alturaplus),
                                           'maptype': 'satellite',
                                           'sensor': 'false',
                                           'scale': str(scale),
                                           'key': api_key})

            surl = 'http://maps.google.com/maps/api/staticmap?' + surlparams
            # rurl = 'http://maps.google.com/maps/api/staticmap?' + rurlparams
            '''
            rurl = 'https://maps.googleapis.com/maps/api/staticmap?key={}&\
center={}&zoom={}&format=png&maptype=roadmap&style=element:geometry%7Ccolor:0xf5f5f5&\
style=element:labels%7Cvisibility:off&style=element:labels.icon%7Cvisibility:off&\
style=element:labels.text.fill%7Ccolor:0x616161&style=element:labels.text.stroke%7Ccolor:0xf5f5f5&\
style=feature:administrative%7Celement:geometry%7Cvisibility:off&style=feature:administrative.land_parcel%7Cvisibility:off&\
style=feature:administrative.land_parcel%7Celement:labels.text.fill%7Ccolor:0xbdbdbd&\
style=feature:administrative.neighborhood%7Cvisibility:off&\
style=feature:landscape.man_made%7Celement:geometry.fill%7Cvisibility:simplified&\
style=feature:poi%7Cvisibility:off&style=feature:poi%7Celement:geometry%7Ccolor:0xeeeeee&\
style=feature:poi%7Celement:labels.text.fill%7Ccolor:0x757575&\
style=feature:poi.park%7Celement:geometry%7Ccolor:0xe5e5e5&\
style=feature:poi.park%7Celement:labels.text.fill%7Ccolor:0x9e9e9e&\
style=feature:road%7Celement:geometry%7Ccolor:0xffffff&\
style=feature:road%7Celement:labels.icon%7Cvisibility:off&\
style=feature:road.arterial%7Celement:labels.text.fill%7Ccolor:0x757575&\
style=feature:road.highway%7Celement:geometry%7Ccolor:0xdadada&\
style=feature:road.highway%7Celement:labels.text.fill%7Ccolor:0x616161&\
style=feature:road.local%7Celement:labels.text.fill%7Ccolor:0x9e9e9e&\
style=feature:transit%7Cvisibility:off&style=feature:transit.line%7Celement:geometry%7Ccolor:0xe5e5e5&\
style=feature:transit.station%7Celement:geometry%7Ccolor:0xeeeeee&\
style=feature:water%7Celement:geometry%7Ccolor:0xc9c9c9&\
style=feature:water%7Celement:geometry.fill%7Ccolor:0x000000&\
style=feature:water%7Celement:labels.text.fill%7Ccolor:0x9e9e9e&\
size={}&scale={}'.format(api_key, position, str(zoom), '%dx%d' % (largura, alturaplus), str(scale))
            '''

            rurl = 'https://maps.googleapis.com/maps/api/staticmap?key={}&\
center={}&zoom={}&format=png&maptype=roadmap&\
style=element:labels%7Cvisibility:off&\
style=feature:administrative%7Celement:geometry%7Cvisibility:off&\
style=feature:administrative.land_parcel%7Cvisibility:off&\
style=feature:administrative.neighborhood%7Cvisibility:off&\
style=feature:landscape.man_made%7Celement:geometry.fill%7Ccolor:0x808080&\
style=feature:landscape.man_made%7Celement:geometry.stroke%7Cvisibility:off&\
style=feature:poi%7Cvisibility:off&style=feature:road%7Celement:geometry.fill%7Ccolor:0x808080&\
style=feature:road%7Celement:geometry.stroke%7Cvisibility:off&\
style=feature:road%7Celement:labels.icon%7Cvisibility:off&\
style=feature:transit%7Cvisibility:off&\
style=feature:transit%7Celement:geometry.fill%7Ccolor:0x808080&\
style=feature:transit%7Celement:geometry.stroke%7Cvisibility:off&\
style=feature:water%7Celement:geometry.fill%7Ccolor:0x000000&\
size={}&scale={}'.format(api_key, position, str(zoom), '%dx%d' % (largura, alturaplus), str(scale))

            s = urllib.urlopen(surl)
            sim = Image.open(StringIO.StringIO(s.read()))

            r = urllib.urlopen(rurl)
            rim = Image.open(StringIO.StringIO(r.read()))

            satellite_final.paste(sim, (int(x*largura), int(y*altura)))
            road_final.paste(rim, (int(x*largura), int(y*altura)))
    satellite_final.show()
    road_final.show()

if __name__ == '__main__':
    print api_key
    get_map()