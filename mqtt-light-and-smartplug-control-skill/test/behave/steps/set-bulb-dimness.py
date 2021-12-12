from behave import given

from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance

# Documentation: https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/custom-steps


@given('{light_name} has been set to {amount} percent brightness.')
@given('{light_name} has been set to {amount} percent dimness.')
@given('{light_name} is shining at {amount} percent brightness.')
def given_set_brightness(context, light_name, amount):
    # check to make sure things are in the proper state with MQTT
    pass
