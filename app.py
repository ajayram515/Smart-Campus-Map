from flask import Flask, render_template, jsonify, request
import json

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
        vehicle_json[new_vehicle_json["vehicle_id"]] = {"lat": new_vehicle_json["lat"], "lon": new_vehicle_json["lon"]}
        vehicle_data = open("vehicle_data.txt", 'w')
        vehicle_data.write(json.dumps(vehicle_json))
        return jsonify({"status":1})
    else:
        vehicle_data = open("vehicle_data.txt", 'r')
        vehicle_json = json.loads(vehicle_data.read())
        vehicle_data.close()
        return jsonify(vehicle_json)

if __name__ == '__main__':
    app.run()
