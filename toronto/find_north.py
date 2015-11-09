# find_north.py
# Find all buses that are travelling northbound of Dave' office
dariush_latitude = 43.65118
dariush_longtitude = -79.3904604
from xml.etree.ElementTree import parse

doc = parse('PublicXMLFeed.xml')
for vehicle in doc.findall('id'):
    v_id = vehicle.findtext('id')
#        if direction.startswith('North'):
#            busid =  bus.findtext('id')
    print(v_id)
