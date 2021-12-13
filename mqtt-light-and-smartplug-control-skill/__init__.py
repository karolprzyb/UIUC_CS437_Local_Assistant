from mycroft import MycroftSkill, intent_file_handler

# Skill-specific dependencies:
from mycroft.util import LOG
import paho.mqtt.client as mqttClient
import time


connected = False
outValue = [0.0, 0.0, 0.0, 0.0]

MQTT_TOPICS_SUB = [("kauf-plug/sensor/kauf_plug_power/state", 0), ("kauf-plug/sensor/kauf_plug_current/state", 0),
                   ("kauf-plug/sensor/kauf_plug_voltage/state", 0), ("kauf-plug/sensor/kauf_plug_total_daily_energy/state", 0)]
TOPICS_INDEX = ["kauf-plug/sensor/kauf_plug_power/state", "kauf-plug/sensor/kauf_plug_current/state",
                "kauf-plug/sensor/kauf_plug_voltage/state", "kauf-plug/sensor/kauf_plug_total_daily_energy/state"]
GOT_INDEX = [False, False, False, False]


class MqttLightAndSmartplugControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.broker = "192.168.1.130"
        self.port = 1883
        self.client = mqttClient.Client("my_uniq_id_1936")

    """
    Initializations that rely on other Mycroft Skills go here if there are any
    """

    def initialize(self):
        pass

    """
    each intent must have its own .intent file with possible inputs and .dialog
    file with possible outputs
    """
    """
    @intent_file_handler('set.bulb.dimness.intent')
    def handle_set_bulb_dimness(self, message):
        amount = message.data.get('amount')  # % brightness
        light_name = message.data.get('light_name')  # identifies the different bulbs

        # do stuff with these variables here

        self.speak_dialog('set.bulb.dimness', data={
            'amount': amount,
            'light_name': light_name
        })
    """

    """
    @intent_file_handler('turn.bulb.on.intent')
    def handle_turn_bulb_on(self, message):
        light_name = message.data.get('light_name')  # identifies the different bulbs

        # do stuff with these variables here

        self.speak_dialog('turn.bulb.on', data={
            'light_name': light_name
        })
    """

    """
    @intent_file_handler('turn.bulb.off.intent')
    def handle_turn_bulb_off(self, message):
        light_name = message.data.get('light_name')  # identifies the different bulbs

        # do stuff with these variables here

        self.speak_dialog('turn.bulb.off', data={
            'light_name': light_name
        })
    """

    @intent_file_handler('set.bulb.color.intent')
    def handle_set_bulb_color(self, message):
        color = message.data.get('color')
        # identifies the different bulbs
        light_name = message.data.get('light_name')

        # do stuff with these variables here
        if light_name != "molly":
            self.speak_dialog('invalid.device', data={
                'device_name': light_name
            })
            return

        if color == "red":
            c = "LA/bulb_1/r_col"
        elif color == "blue":
            c = "LA/bulb_1/b_col"
        elif color == "green":
            c = "LA/bulb_1/g_col"
        else:
            self.speak_dialog('invalid.color', data={
                'color': color
            })
            return

        self.client.on_connect = run_on_connect
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

        while(not(connected)):
            self.log.info(connected)
            time.sleep(0.1)

        try:
            msg_val = '1'
            self.client.publish(c, msg_val)
            # time.sleep(3.0)
        except KeyboardInterrupt:
            self.log.error("exiting")
            self.client.disconnect()

        self.log.info("Exiting")
        self.client.disconnect()
        self.client.loop_stop()

        self.speak_dialog('set.bulb.color', data={
            'color': color,
            'light_name': light_name
        })

    """
    @intent_file_handler('identify.bulb.intent')
    def handle_identify_bulb(self, message):
        light_name = message.data.get('light_name')  # identifies the different bulbs

        # do stuff with these variables here

        self.speak_dialog('identify.bulb', data={
            'light_name': light_name
        })
    """

    @intent_file_handler('get.plug.stats.intent')
    def handle_get_plug_stats(self, message):
        # identifies the different plugs
        smartplug_name = message.data.get('smartplug_name')

        # do stuff with these variables here
        if smartplug_name != "jeff":
            self.speak_dialog('invalid.device', data={
                'device_name': smartplug_name,
            })
            return

        self.client.on_connect = run_on_connect
        self.client.on_message = run_on_message
        self.client.connect(self.broker, self.port)

        try:
            while GOT_INDEX != [True, True, True, True]:
                self.client.loop_start()
                while(not(connected)):
                    time.sleep(0.05)

                #self.log.info(mqttClient.MQTT_ERR_SUCCESS)
                #self.log.info(self.client.subscribe(MQTT_TOPICS_SUB))
                self.client.subscribe(MQTT_TOPICS_SUB)
                self.client.loop_stop()
            self.log.info(outValue)

        except KeyboardInterrupt:
            self.log.error("exiting")
            self.client.disconnect()
            self.client.loop_stop()

        self.speak_dialog('get.plug.stats', data={
            'a': outValue[1],
            'kwh': outValue[3],
            'w': outValue[0],
            'v': outValue[2],
            'smartplug_name': smartplug_name
        })

    @intent_file_handler('turn.plug.on.intent')
    def handle_turn_plug_on(self, message):
        # identifies the different plugs
        smartplug_name = message.data.get('smartplug_name')

        # do stuff with these variables here
        if smartplug_name == "jeff":
            topic = "LA/plug_1/power"
        elif smartplug_name == "molly":
            topic = "LA/bulb_1/light"
        else:
            self.speak_dialog('invalid.device', data={
                'device_name': smartplug_name
            })
            return

        self.client.on_connect = run_on_connect
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

        while(not(connected)):
            self.log.info(connected)
            time.sleep(0.1)

        msg_val = '1'
        self.client.publish(topic, msg_val)

        self.log.info("Disconnecting")
        self.client.disconnect()
        self.client.loop_stop()

        self.speak_dialog('turn.plug.on', data={
            'smartplug_name': smartplug_name
        })

    @intent_file_handler('turn.plug.off.intent')
    def handle_turn_plug_off(self, message):
        # identifies the different plugs
        smartplug_name = message.data.get('smartplug_name')

        # do stuff with these variables here
        if smartplug_name == "jeff":
            topic = "LA/plug_1/power"
        elif smartplug_name == "molly":
            topic = "LA/bulb_1/light"
        else:
            self.speak_dialog('invalid.device', data={
                'device_name': smartplug_name
            })
            return

        self.client.on_connect = run_on_connect
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

        while(not(connected)):
            self.log.info(connected)
            time.sleep(0.1)

        msg_val = '0'
        self.client.publish(topic, msg_val)

        self.log.info("Disconnecting")
        self.client.disconnect()
        self.client.loop_stop()

        self.speak_dialog('turn.plug.off', data={
            'smartplug_name': smartplug_name
        })

    """
    It's also possible to have "Converse" methods for handling followup
    utterances a user might make. We may want to write one of these in case a
    user's utterance can't be understood but I haven't written any yet.
    """

    """
    Things that need to occur if a user asks Mycroft to stop doing the skill go
    here
    """

    def stop(self):
        pass

    """
    Things that need to happen when the skill terminates go here
    """

    def shutdown(self):
        pass


def create_skill():
    return MqttLightAndSmartplugControl()


def run_on_connect(client, userdata, flags, rc):
    if rc == 0:
        global connected
        connected = True
        LOG.info(connected)
        LOG.info("Connected...")
    else:
        LOG.info("Connection failed")


def run_on_message(client, userdata, message):
    #LOG.info("Got a message")
    #LOG.info("Topic: " + str(message.topic))
    #LOG.info("Wattage: " + str(message.payload))
    #LOG.info("=============================================================")
    global TOPICS_INDEX
    global GOT_INDEX
    global outValue
    for x in range(4):
        if str(message.topic) == TOPICS_INDEX[x]:
            outValue[x] = float(message.payload)
            GOT_INDEX[x] = True
            #LOG.info('GOT ONE')
