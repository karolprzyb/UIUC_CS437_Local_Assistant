from behave import given

from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance

# Documentation: https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/custom-steps


@given('{smartplug_name} is operating at {a} amps, {w} watts, and {v} volts. It has used {kwh} kilowatt-hours of energy today.')
@given('{smartplug_name} is operating at {a} amperes, {w} watts, and {v} volts. It has used {kwh} kilowatt-hours of energy today.')
def given_get_plug_stats(context, smartplug_name, a, w, v, kwh):
    # check to make sure things are in the proper state with MQTT
    pass
