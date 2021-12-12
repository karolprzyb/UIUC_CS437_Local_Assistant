from mycroft import MycroftSkill, intent_file_handler


class MqttLightAndSmartplugControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    
    """
    Initializations that rely on other Mycroft Skills go here if there are any
    """
    def initialize(self):
        pass


    """
    each intent must have its own .intent file with possible inputs and .dialog
    file with possible outputs
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


    @intent_file_handler('turn.bulb.on.intent')
    def handle_turn_bulb_on(self, message):
        light_name = message.data.get('light_name')  # identifies the different bulbs

        # do stuff with these variables here

        self.speak_dialog('turn.bulb.on', data={
            'light_name': light_name
        })


    @intent_file_handler('turn.bulb.off.intent')
    def handle_turn_bulb_off(self, message):
        light_name = message.data.get('light_name')  # identifies the different bulbs

        # do stuff with these variables here

        self.speak_dialog('turn.bulb.off', data={
            'light_name': light_name
        })

    
    @intent_file_handler('set.bulb.color.intent')
    def handle_set_bulb_color(self, message):
        color = message.data.get('color')
        light_name = message.data.get('light_name')  # identifies the different bulbs

        # do stuff with these variables here

        self.speak_dialog('set.bulb.color', data={
            'color': color,
            'light_name': light_name
        })


    @intent_file_handler('identify.bulb.intent')
    def handle_identify_bulb(self, message):
        light_name = message.data.get('light_name')  # identifies the different bulbs

        # do stuff with these variables here

        self.speak_dialog('identify.bulb', data={
            'light_name': light_name
        })


    @intent_file_handler('get.plug.stats.intent')
    def handle_get_plug_stats(self, message):
        smartplug_name = message.data.get('smartplug_name')  # identifies the different plugs

        # do stuff with these variables here
        a = None
        kwh = None
        w = None
        v = None

        self.speak_dialog('get.plug.stats', data={
            'a': a,
            'kwh': kwh,
            'w': w,
            'v': v,
            'smartplug_name': smartplug_name
        })


    @intent_file_handler('turn.plug.on.intent')
    def handle_turn_plug_on(self, message):
        smartplug_name = message.data.get('smartplug_name')  # identifies the different plugs

        # do stuff with these variables here

        self.speak_dialog('turn.plug.on', data={
            'smartplug_name': smartplug_name,
        })


    @intent_file_handler('turn.plug.off.intent')
    def handle_turn_plug_off(self, message):
        smartplug_name = message.data.get('smartplug_name')  # identifies the different plugs

        # do stuff with these variables here

        self.speak_dialog('turn.plug.off', data={
            'smartplug_name': smartplug_name,
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