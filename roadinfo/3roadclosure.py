__author__ = 'Dariush Azimi'

# Find all closures that are close to Dariush
# Nov 8, 2015


#import os
from datetime import date, datetime, time, timedelta
import arrow
import colorama
from colorama import Fore, Back, Style
from xml.etree.ElementTree import parse
import time

from pprint import pprint

from dateutil import parser

import convertlonglatDistanceTokm

DistanceFromMe  = int(input("How far from you do you want to see?: "))
DaysFromNow     = int(input("And how many days from now?: "))

print (DistanceFromMe)
print (DaysFromNow)

#DistanceFromMe      = 5 #in KM"
#DaysFromNow         = 2

dariush_latitude    = 43.754816
dariush_longtitude  = -79.408976

#43.7429747,  -79.4750023

Now                 = datetime.now()
colorama.init()

#print(Fore.RED + text)
#print(Back.GREEN + text + Style.RESET_ALL)
#print(text)

doc             = parse('RoadRestrictions.xml')
greenLines = []

for Closure in doc.findall('Closure'):

    StartTime = int(Closure.findtext('StartTime'))/1000
    StartTime = arrow.get(StartTime)
    differenceInTime = StartTime.date() - Now.date()
    if  differenceInTime.days>0:
        lat         = float(Closure.findtext('Latitude'))
        lon         = float(Closure.findtext('Longitude'))

        district    = Closure.findtext('District')
        EndTime     = Closure.findtext('EndTime')
        name        = Closure.findtext('Name')

        inKm        = int(convertlonglatDistanceTokm.distance_on_unit_sphere(dariush_latitude,dariush_longtitude, lat,lon))
        if inKm<DistanceFromMe:
            print(Fore.RED + name, district, inKm, "km:", "Closed ", StartTime.humanize())
        else:
            #greenLines.append = input(Fore.GREEN + name, district, inKm, "km:", "closed starting ", StartTime.humanize())
            print(Fore.GREEN + name, district, inKm, "km:", "closed starting ", StartTime.humanize())
            #pprint(greenLines)
#print(greenLines)