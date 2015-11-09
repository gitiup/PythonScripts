import urllib.request as ur
import pprint
#filehandler = ur.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=ttc&r=505&t=1307558878000')

filehandler = ur.urlopen('http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=ttc&t=1446833222490')
data =filehandler.read()
f = open('publicXMLFeed.xml', 'wb')
f.write(data)
f.close()
pprint.pprint(data)