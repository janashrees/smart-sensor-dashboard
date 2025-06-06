from flask import Flask, request, jsonify
from flask_cors import CORS  # ✅ NEW

from datetime import datetime

app = Flask(__name__)
CORS(app)  # ✅ NEW - Allow requests from other origins like localhost:3000

sensor_data_log = []

@app.route('/api/sensor-data', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    data['timestamp'] = datetime.utcnow().isoformat()
    sensor_data_log.append(data)
    print(f"Received: {data}")
    return jsonify({"message": "Data received"}), 200

@app.route('/api/sensor-data', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data_log), 200

if __name__ == '__main__':
    app.run(debug=True)
