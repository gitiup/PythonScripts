# monitor.py

import urllib.request as ur
from time import gmtime, strftime

from xml.etree.ElementTree import parse
# http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=ttc&r=501

candidates = ['1783', '1709', '1413', '1895','1720', '1911']
daves_latitude = 41.877176012311665

def distance(lat1, lat2):
    'return distance in minles between two lats'
    return round(1.60934*69*abs(lat1 - lat2), 4)

def monitor():
    filehandler = ur.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(filehandler)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        direction_x = bus.findtext('dd')
        if busid in candidates:
            lat =  float(bus.findtext('lat'))
            dis = distance(lat, daves_latitude)

            #if distance is closer, send an alert.

            if dis<0.8:
                print(busid, dis, 'km', strftime("%Y-%m-%d %H:%M:%S", gmtime()), "ALERT"*10)
            else:
                print(busid,direction_x, dis, 'km', strftime("%Y-%m-%d %H:%M:%S", gmtime()))

            print('-'*10)

import time
while True:
    monitor()
    time.sleep(10)
    print('+'*40)



