import time
import random
import requests

URL = "http://127.0.0.1:5000/api/sensor-data"

def generate_sensor_data():
    return {
        "device_id": "sim-001",
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "gas_level": round(random.uniform(100, 300), 2)
    }

while True:
    data = generate_sensor_data()
    try:
        response = requests.post(URL, json=data)
        print(f"Sent data: {data}, Response: {response.status_code}")
    except Exception as e:
        print(f"Failed to send data: {e}")
    time.sleep(5)
