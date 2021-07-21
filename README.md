## Azure IOT Hub fundamentals and MQTT support

Although the IOT hub of azure enables devices to communicate with the IoT Hub device endpoints using two methods but still it is not a full-featured MQTT broker and does not support all the behaviors specified in the MQTT v3.1.1 standard.

The two methods to communicate to Azure iot hub are:-

1. MQTT v3.1.1 on port 8883
2. MQTT v3.1.1 over WebSocket on port 443.

To communicate using MQTT to azure IOT hub there are two ways to so:
- Libraries in the Azure IoT SDKs.
- The MQTT protocol directly.

As MQTT port (8883) is blocked in many corporate and educational networking environments. Hence we can use MQTT over Web Sockets. MQTT over Web Sockets communicates over port 443, which is almost always open in networking environments.
