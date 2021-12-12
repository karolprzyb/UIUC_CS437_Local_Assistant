from behave import given

from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance

# Documentation: https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/custom-steps


@given('{light_name} is flashing on and off.')
@given('{light_name} is flashing.')
@given('{light_name} is blinking.')
def given_identify_bulb(context, light_name):
    # check to make sure things are in the proper state with MQTT
    pass
