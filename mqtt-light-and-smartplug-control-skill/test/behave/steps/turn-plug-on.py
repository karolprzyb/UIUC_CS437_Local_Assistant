from behave import given

from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance

# Documentation: https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/custom-steps


@given('{smartplug_name} is on.')
@given('{smartplug_name} is now on.')
@given('{smartplug_name} has been turned on.')
@given('{smartplug_name} was turned on.')
@given('{smartplug_name} has been activated.')
@given('{smartplug_name} was activated.')
def given_turn_on(context, smartplug_name):
    # check to make sure things are in the proper state with MQTT
    pass
