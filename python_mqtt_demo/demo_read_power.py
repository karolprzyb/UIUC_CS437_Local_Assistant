import paho.mqtt.client as mqttClient
import time
broker = "192.168.1.75"
port = 1883
client = mqttClient.Client("my_uniq_id_1936")
connected = False
waitingMessage = True

MQTT_TOPICS_SUB = [("kauf-plug/sensor/kauf_plug_power/state",0),("kauf-plug/sensor/kauf_plug_current/state",0),("kauf-plug/sensor/kauf_plug_voltage/state",0), ("kauf-plug/sensor/kauf_plug_total_daily_energy/state",0)]

def run_on_connect(client, userdata, flags, rc):
    if rc == 0:
        global connected 
        connected = True
        print("Connected...")
    else:
        print("Connection failed")
    
def run_on_message(client, userdata, message):
    print("Got a message")
    print("Topic: " + str(message.topic))
    print("Wattage: " + str(message.payload))
    print("=============================================================")
    if str(message.topic) == "kauf-plug/sensor/kauf_plug_voltage/state":
        global waitingMessage
        waitingMessage = False
        print('DONE')
    
client.on_connect = run_on_connect
client.on_message = run_on_message
#client.on_publish = run_on_publish
#client.on_subscribe = run_on_subscribe
client.connect(broker, port)

try:
    while waitingMessage:
        print(waitingMessage)
        client.loop_start()
        while(not(connected)):
            time.sleep(0.05)

        #print(mqttClient.MQTT_ERR_SUCCESS)
        print(client.subscribe(MQTT_TOPICS_SUB))
        client.loop_stop();

except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()