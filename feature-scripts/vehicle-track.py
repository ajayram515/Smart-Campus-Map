#! /usr/bin/python

from gps import *
import requests
import time
vehicle_id="test-rickshaw"
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
proxies = {'http': 'http://pavan71198:h4ck3r@202.141.80.20:3128','https': 'http://pavan71198:h4ck3r@202.141.80.20:3128'}
try:         
    while True:
        report = gpsd.next()
        if report['class'] == 'TPV':
            headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
            json_data = {"vehicle_id":vehicle_id,"lat":getattr(report,'lat',0.0),"lon":getattr(report,'lon',0.0)}
            print json_data
            post_request = requests.post(url="http://0eaacd45.ngrok.io/vehicle_track",data=json.dumps(json_data), headers=headers, proxies=proxies)
        time.sleep(1)
except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "Done.\nExiting."
