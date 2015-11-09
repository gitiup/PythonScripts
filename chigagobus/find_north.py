# find_north.py
# Find all buses that are travelling northbound of Dave' office
daves_latitude = 41.877176012311665
daves_longtitude = -87.6291046142578

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    lat =  float(bus.findtext('lat'))
    if lat> daves_latitude:
        direction = bus.findtext('d')
        if direction.startswith('North'):
            busid =  bus.findtext('id')
            print(busid, lat)