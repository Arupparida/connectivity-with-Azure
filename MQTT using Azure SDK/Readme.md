# connectivity-with-Azure with AZURE IOT_HUB_SDK

connect to Raspberry pie to Azure iot hub.

Step 1
Installing important packages needed to connect to Azure IOT hub using Python on the raspberry pi.

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



