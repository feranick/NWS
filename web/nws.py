#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
**********************************************
* NWS
* v2024.01.09.1
* By: Nicola Ferralis <feranick@hotmail.com>
**********************************************
'''
#print(__doc__)

#from pymbta3 import Stops, Vehicles
#from geopy.geocoders import Nominatim
from datetime import datetime
import pytz, tzlocal
import sys, requests
    
#************************************
''' Params '''
#************************************
class Conf:
    def __init__(self):
        self.url = "https://api.weather.gov/"
        self.user_agent = "(feranick, feranick@hotmail.com)"
        self.headers = {'Accept': 'application/geo+json',
            'User-Agent' : self.user_agent}

#************************************
''' Main '''
#************************************
def main():
    if len(sys.argv) > 1:
        getNWSData(sys.argv[1])
    else:
        return
    
def getNWSData(station):
    wdata = requests.get(Conf().url+"stations/"+station+"/observations/latest/", headers=Conf().headers).json()
    
    #print(wdata)
    dt = datetime.strptime(wdata['properties']['timestamp'],
        "%Y-%m-%dT%H:%M:%S+%f:00")
    local_dt = dt.replace(tzinfo=pytz.utc).astimezone(tzlocal.get_localzone())
    
    print("\nStation: ",sys.argv[1])
    print("Elevation: %d meters" % intN(wdata['properties']['elevation']['value']))
    print("Timestamp:",local_dt)
    print("\nTemperature: %0.1f degC" % floatN(wdata['properties']['temperature']['value']))
    print("Relative humidity: %0.1f %%" % floatN(wdata['properties']['relativeHumidity']['value']))
    print("Dew point: %0.1f degC" % floatN(wdata['properties']['dewpoint']['value']))
    print("Wind speed: %0.1f km/h" % floatN(wdata['properties']['windSpeed']['value']))
    #print("Wind gust: %0.1f" % float(wdata['properties']['windGust']['value']))
    #print("Heat Index: %0.2f degC" % floatN(wdata['properties']['heatIndex']['value']))
    print("Wind Chill: %0.1f degC" % floatN(wdata['properties']['windChill']['value']))
    print("\nBarometric Pressure: %0.2f hPa" % (floatN(wdata['properties']['barometricPressure']['value'])/100))
    print("Sea-Level Pressure: %0.2f hPa\n" % (floatN(wdata['properties']['seaLevelPressure']['value'])/100))
    
def intN(a):
    if a is not None:
        return int(a)
    else:
        return 0
        
def floatN(a):
    if a is not None:
        return float(a)
    else:
        return 0
        
#************************************
''' Main initialization routine '''
#************************************
if __name__ == "__main__":
    sys.exit(main())
