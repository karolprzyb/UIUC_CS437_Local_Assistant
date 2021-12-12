from behave import given

from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance

# Documentation: https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/custom-steps


@given('{light_name} is off.')
@given('{light_name} is now off.')
@given('{light_name} has been turned off.')
@given('{light_name} was turned off.')
def given_turn_off(context, light_name):
    # check to make sure things are in the proper state with MQTT
    pass
