from behave import given

from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance

# Documentation: https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/custom-steps


@given('{smartplug_name} is off.')
@given('{smartplug_name} is now off.')
@given('{smartplug_name} has been turned off.')
@given('{smartplug_name} was turned off.')
@given('{smartplug_name} has been deactivated.')
@given('{smartplug_name} was powered off.')
def given_turn_off(context, smartplug_name):
    # check to make sure things are in the proper state with MQTT
    pass
