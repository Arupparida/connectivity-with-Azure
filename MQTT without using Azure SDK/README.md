# Azure Documentation 

Link: [Azure MQTT DOCUMENTATION](https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support)

## Using the MQTT protocol directly (as a device)

A device can connect to Azure IOT hub directly without using SDKs by connecting  to the public device endpoints using the MQTT protocol on port 8883.

The CONNECT packet has to be configured for the same:-
- For the ClientId field, use the deviceId.
- For the Username field, use {iothubhostname}/{device_id}/?api-version=2018-06-30, where {iothubhostname} is the full CName of the IoT hub.
- For example, if the name of your IoT hub is contoso.azure-devices.net and if the name of your device is MyDevice01, the full Username field should contain:
contoso.azure-devices.net/MyDevice01/?api-version=2018-06-30
 - For the Password field, use a SAS token. The format of the SAS token is the same as for both the HTTPS and AMQP protocols.
 
To understand how the SAS token works we need to refer to Azure IOT hub security tokens and to generate SAS token we can find options available in the Azure IOT hub portal with “Generate SAS Token for Device” option.

The “Operations Monitoring channel” helps to monitor the connect and disconnect packs of MQTT over Azure IOT HUB. This features additional information that can help you to troubleshoot connectivity issues(like the different parameters in the connect packet).

