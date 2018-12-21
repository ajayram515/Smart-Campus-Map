from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vehicle_track', methods=['POST','GET'])
def vehicle_track():
    if request.method == 'POST':
        new_vehicle_json = request.get_json()
        vehicle_data = open("vehicle_data.txt", 'r')
        vehicle_json = json.loads(vehicle_data.read())
        vehicle_data.close()
        vehicle_json[new_vehicle_json["vehicle_id"]] = {"lat": new_vehicle_json["lat"], "lon": new_vehicle_json["lon"], "timestamp": int(datetime.now().timestamp())}
        vehicle_data = open("vehicle_data.txt", 'w')
        vehicle_data.write(json.dumps(vehicle_json))
        vehicle_data.close()
        return jsonify({"status":1})
    else:
        vehicle_data = open("vehicle_data.txt", 'r')
        vehicle_json = json.loads(vehicle_data.read())
        vehicle_data.close()
        return jsonify(vehicle_json)

@app.route('/mqtt_data', methods=['POST','GET'])
def mqtt_data():
    if request.method == 'POST':
        new_mqtt_json = request.get_json()
        mqtt_data = open("mqtt_data.txt", 'r')
        mqtt_json = json.loads(mqtt_data.read())
        mqtt_data.close()
        mqtt_json[new_mqtt_json["mqtt_id"]] = {"lat": new_mqtt_json["lat"], "lon": new_mqtt_json["lon"], "data": new_mqtt_json["data"], "timestamp": int(datetime.now().timestamp())}
        mqtt_data = open("mqtt_data.txt", 'w')
        mqtt_data.write(json.dumps(mqtt_json))
        mqtt_data.close()
        return jsonify({"status": 1})
    else:
        mqtt_data = open("mqtt_data.txt", 'r')
        mqtt_json = json.loads(mqtt_data.read())
        mqtt_data.close()
        return jsonify(mqtt_json)
if __name__ == '__main__':
    app.run()
