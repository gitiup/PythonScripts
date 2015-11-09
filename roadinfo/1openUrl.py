#! Python2.7

__author__ = 'Dariush Azimi'

# Find all closures that are close to Dariush
# Nov 8, 2015


import urllib.request as ur
import pprint
#filehandler = ur.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=ttc&r=505&t=1307558878000')

filehandler     = ur.urlopen('http://www1.toronto.ca/transportation/roadrestrictions/RoadRestrictions.xml')
data            = filehandler.read()
f               = open('RoadRestrictions.xml', 'wb')
f.write(data)
f.close()
pprint.pprint(data)