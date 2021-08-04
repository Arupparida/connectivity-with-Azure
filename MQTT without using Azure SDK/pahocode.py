import logging
from paho.mqtt import client as mqtt
import ssl

logging.basicConfig(filename='example.log', level=logging.DEBUG)
log=logging.getLogger("Myapp")

path_to_root_cert = "/home/pi/azureiot/BaltimoreCyberTrustRoot.crt.pem"
device_id = "raspi49"
sas_token="SharedAccessSignature sr=tima.azure-devices.net%2Fdevices%2Fraspi49&sig=skGljNir3NtVK%2FD3Q%2FXurWQ0c%2BOc%2FqvlifY8ucsr0UA%3D&se=1640490873"


iot_hub_name = "<Add your hub name>"
def on_connect(client, userdata, flags, rc):
    print("Device connected with result code: " + str(rc))


def on_disconnect(client, userdata, rc):
    print("Device disconnected with result code: " + str(rc))


def on_publish(client, userdata, mid):
    print("Device sent message")


client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)
ecg}YC$710Blocked for client.enable_logger(log)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

client.username_pw_set(username=iot_hub_name+".azure-devices.net/" +
                       device_id + "/?api-version=2018-06-30", password=sas_token)

client.tls_set(ca_certs=path_to_root_cert, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
#               cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
client.tls_insecure_set(False)

client.connect(iot_hub_name+".azure-devices.net", port=8883)
client.publish("devices/" + device_id + "/messages/events/", '{"id":123}', qos=1)
client.publish("devices/" + device_id + "/messages/events/", '{"id":123}', qos=1)
client.loop_forever()



