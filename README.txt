Group-19 :: Smart Campus Map

Two features have been implemented :
1) Vehicle Tracking
2) Room Count

A server is hosted at the lab. By running the flask server using the devel-flask.sh script after installing the requirements in requirements.txt in a Python 3 virtualenv.
On the server homepage http://127.0.0.1:5000 we display all the data we recieve from the Raspberry Pis

The features are run on Raspberry Pi by running the files at the given paths and both are written in Python 2.
Vehicle Tracking : A GPS sensor is mounted on the Pi which in turn is used to track an vehicle.
Features :
1) We made the Pi mobile against the previously stationary pi idea located at the lab.
2) We get location through GPS module and mark it on the google maps server hosted.
Requires installation gpsd from apt
file : feature-scripts/vehicle-track.py

Room Count : A pi will be located on doors of the rooms to keep the count of number of people inside a particular room.
Features :
1) A two IR sensor system are used for getting accurate count considering various cases.

file : feature-scripts/room-count.py
