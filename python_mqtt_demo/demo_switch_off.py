import paho.mqtt.client as mqttClient
import time
broker = "192.168.1.75"
port = 1883
client = mqttClient.Client("my_uniq_id_1936")
def run_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected...")
        msg_val = '0';
        topic = "LA/plug_1/power"
        client.publish(topic, msg_val)
    else:
        print("Connection failed")
    client.disconnect()
    client.loop_stop()
    
client.on_connect = run_on_connect
client.connect(broker, port)
client.loop_start()
time.sleep(3);