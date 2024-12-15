# connectivity-with-Azure with AZURE IOT_HUB_SDK

## connect to Raspberry pie to Azure iot hub.

 Step 1

/ Installing important packages needed to connect to Azure IOT hub using Python on the raspberry pi.

sudo pip3 install azure-iot-device

sudo pip3 install azure-iot-hub

sudo pip3 install azure-iothub-service-client

sudo pip3 install azure-iothub-device-client 


All these packages may not necessarily be required to get the telemetry on the azure but it is recommended for no error issue.

Step 2 
Create an IOT hub on Azure portal and register a new device.

To create an IOt hub follow the below steps or refer to the following link- Use the Azure portal to create an IoT Hub 
 
Sign in to the Azure portal.
From the Azure homepage, select the + Create a resource button, and then enter IoT Hub in the Search the Marketplace field.
Select IoT Hub from the search results, and then select Create.
On the Basics tab, complete the fields as follows:(In my case)
  1) Subscription: Azure for students
  2)Resource Group: Cloud shell storage central india
  3)Region: Nearest region 
  4)IoT Hub Name: desired iot hub name
  Next: Networking tab (keep things in default)
Next: Management tab 
Pricing and scale tier : Free tier
Rest keep default
Next tags tab (keep default)
Click review and create
Click Go to resources.
Now click on the “IOT devices” tab in the explorer section of IOT hub.
Select New to add a device in your IoT hub.
In Create a device, provide a name for your new device and select Save.
Once the  device is created, click on the device name in the IoT devices pane. Copy the Primary Connection String. This connection string is used by device code to communicate with the hub.
 
 Step 3
Configure Raspberry pi and Azure for connection
Write python code(code that generates sample sensor data) to run on the azure CLI. 
Import the code to Raspberry pi
Run the code in the python ide of raspberry pi.
Check for the results 
Now use the  Azure CLI packages , install the same on the cloud terminal ,the following  link can help in the same -Quickstart - Send telemetry to Azure IoT Hub (CLI) quickstart 
Or alternatively run the following commands on the Azure cloud shell
Install the CLI extensions to add the Microsoft Azure IoT Extension for Azure CLI to your CLI shell. The IOT Extension adds IoT Hub, IoT Edge, and IoT Device Provisioning Service (DPS) specific commands to Azure CLI.
Cmd: az extension add --name azure-iot

Cmd : az iot hub monitor-events --output table --hub-name iotrial
Replace iotrial with your iothubname
Now run the following command to monitor and see the sensor data on the azure CLI portal 
Cmd : az iot hub monitor-events --hub-name iotrial --device-id Testberry
Replace Testberry with your device id.


# Benefits of using Azure IOT SDKs

The device SDKs helps in enabling the connected device to exchange messages with the Azure IOT hub. The device SDKs use the standard IoT Hub connection string to establish a connection to an IoT hub. Device SDKs  supports the MQTT protocol  available for Java, Node.js, C, C#, and Python. 

Now there are certain parameter that has to be set to use the MQTT protocol using the azure IOT device SDKs.
- The client protocol parameter must be set to MQTT.
- You can also specify MQTT over Web Sockets in the client protocol parameter.
By default, the device SDKs connect to an IoT Hub with the CleanSession flag set to 0 and use QoS 1 for message exchange with the IoT hub. It can also be changed to Qos 0.


