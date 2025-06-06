import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [sensorData, setSensorData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/sensor-data")
      .then((res) => res.json())
      .then((data) => setSensorData(data))
      .catch((err) => console.error("Fetch error:", err));
  }, []);

  return (
    <div className="App">
      <h1>Sensor Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>Device ID</th>
            <th>Temperature (°C)</th>
            <th>Humidity (%)</th>
            <th>Gas Level</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          {sensorData.map((entry, index) => (
            <tr key={index}>
              <td>{entry.device_id}</td>
              <td>{entry.temperature}</td>
              <td>{entry.humidity}</td>
              <td>{entry.gas_level}</td>
              <td>{entry.timestamp}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
