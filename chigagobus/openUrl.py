import urllib.request as ur
import pprint
filehandler = ur.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data =filehandler.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()
pprint.pprint(data)