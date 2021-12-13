import paho.mqtt.client as mqttClient
import time
broker = "192.168.1.75"
port = 1883
client = mqttClient.Client("my_uniq_id_1936")
connected = False
outValue = [0.0,0.0,0.0,0.0]
#voltageValue = 0.0
#currentValue = 0.0
#powerValue = 0.0
#energyValue = 0.0

MQTT_TOPICS_SUB = [("kauf-plug/sensor/kauf_plug_power/state",0),("kauf-plug/sensor/kauf_plug_current/state",0),("kauf-plug/sensor/kauf_plug_voltage/state",0), ("kauf-plug/sensor/kauf_plug_total_daily_energy/state",0)]
TOPICS_INDEX = ["kauf-plug/sensor/kauf_plug_power/state", "kauf-plug/sensor/kauf_plug_current/state", "kauf-plug/sensor/kauf_plug_voltage/state", "kauf-plug/sensor/kauf_plug_total_daily_energy/state"]
GOT_INDEX = [False, False, False, False]

def run_on_connect(client, userdata, flags, rc):
    if rc == 0:
        global connected 
        connected = True
        print("Connected...")
    else:
        print("Connection failed")
    
def run_on_message(client, userdata, message):
    #print("Got a message")
    #print("Topic: " + str(message.topic))
    #print("Wattage: " + str(message.payload))
    #print("=============================================================")
    global TOPICS_INDEX
    global GOT_INDEX
    global outValue
    for x in range(4):
        if str(message.topic) == TOPICS_INDEX[x]:
            outValue[x] = float(message.payload)
            GOT_INDEX[x] = True
            #print('GOT ONE')
    
client.on_connect = run_on_connect
client.on_message = run_on_message
#client.on_publish = run_on_publish
#client.on_subscribe = run_on_subscribe
client.connect(broker, port)

try:
    while GOT_INDEX != [True, True, True, True]:
        client.loop_start()
        while(not(connected)):
            time.sleep(0.05)

        #print(mqttClient.MQTT_ERR_SUCCESS)
        #print(client.subscribe(MQTT_TOPICS_SUB))
        client.subscribe(MQTT_TOPICS_SUB)
        client.loop_stop();
    print(outValue)
    
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()