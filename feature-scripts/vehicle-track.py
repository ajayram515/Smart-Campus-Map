#! /usr/bin/python

from gps import *
import requests
import time
vehicle_id="abcd"
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
try:         
    while True:
        report = gpsd.next()
        if report['class'] == 'TPV':
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            json_data = {"vehicle_id":vehicle_id,"lat":getattr(report,'lat',0.0),"lon":getattr(report,'lon',0.0)}
            post_request = requests.post(url="http://127.0.0.1:5000/vehicle_track",data=json.dumps(json_data), headers=headers)
            print post_request.data()
        time.sleep(1)
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "Done.\nExiting."
