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
#import date_converter
#import geocoder
from dateutil import parser

import convertlonglatDistanceTokm

DistanceFromMe  = int(input("How far from you do you want to see?: "))
DaysFromNow     = int(input("And how many days from now?: "))

print (DistanceFromMe)
print (DaysFromNow)

#DistanceFromMe      = 5 #in KM"
#DaysFromNow         = 2

dariush_latitude    = 43.7429747
dariush_longtitude  = -79.4750023


Now                 = datetime.now()
colorama.init()

#print(Fore.RED + text)
#print(Back.GREEN + text + Style.RESET_ALL)
#print(text)

doc             = parse('RoadRestrictions.xml')

for Closure in doc.findall('Closure'):

    #print (Closure.findtext('StartTime'))
    StartTime = int(Closure.findtext('StartTime'))/1000

    #StartTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(StartTime))
    #StartTime = datetime.fromtimestamp(StartTime).strftime('%Y-%m-%d %H:%M:%S')

    StartTime = time.strftime("%a, %d %b %Y %H:%M:%S .0000", time.localtime(StartTime))

    StartTime = parser.parse(StartTime)
    # print (StartTime)
    differenceInTime = StartTime.date() - Now.date()
    #rint(differenceInTime.days)
    if  differenceInTime.days>0:
        lat         = float(Closure.findtext('Latitude'))
        lon         = float(Closure.findtext('Longitude'))

        district    = Closure.findtext('District')
        #StartTime   = Closure.findtext('StartTime')
        EndTime     = Closure.findtext('EndTime')
        #StartTime   = datetime.fromtimestamp(int(StartTime)/1000.)
        name        = Closure.findtext('Name')


        #print(differenceInTime.days)
        #NumberOfDays = int((str(NumberOfDays)  [0]) )
        inKm        = int(convertlonglatDistanceTokm.distance_on_unit_sphere(dariush_latitude,dariush_longtitude, lat,lon))
        if inKm<DistanceFromMe:
            print(Fore.RED + name, district, inKm, "km:", "Closed on ", StartTime, "in ", differenceInTime.days , "day!!!!")
        else:
            print(Fore.GREEN + name, district, inKm, "km:", "closed starting at ", StartTime, "in ", differenceInTime.days , "day")
