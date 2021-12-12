import paho.mqtt.client as mqttClient
import time
broker = "192.168.1.75"
port = 1883
client = mqttClient.Client("my_uniq_id_1936")
connected = False

def run_on_connect(client, userdata, flags, rc):
    if rc == 0:
        global connected
        connected = True
        print(connected)
        print("Connected...")
    else:
        print("Connection failed")
    
client.on_connect = run_on_connect
client.connect(broker, port)
client.loop_start()

while(not(connected)):
    print(connected)
    time.sleep(0.1)

msg_val = '1';
topic = "LA/plug_1/power"
client.publish(topic, msg_val)

print("Exiting")
client.disconnect()
client.loop_stop()