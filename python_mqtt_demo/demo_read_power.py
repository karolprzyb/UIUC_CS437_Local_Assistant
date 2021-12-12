import paho.mqtt.client as mqttClient
import time
broker = "192.168.1.75"
port = 1883
client = mqttClient.Client("my_uniq_id_1936")
connected = False

MQTT_TOPICS_SUB = [("LA/plug1/power_meas",0),("LA/plug1/voltage",0)]

def run_on_connect(client, userdata, flags, rc):
    if rc == 0:
        global connected 
        connected = True
        print("Connected...")
    else:
        print("Connection failed")
    
def run_on_message(client, userdata, message):
    print("Got a message")
    print(client)
    print("Wattage: " + str(message.payload))
    
client.on_connect = run_on_connect
client.on_message = run_on_message
client.connect(broker, port)
client.loop_start()
while(not(connected)):
    time.sleep(0.1)

client.subscribe(MQTT_TOPICS_SUB)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()