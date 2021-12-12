from behave import given

from test.integrationtests.voight_kampff import wait_for_dialog, emit_utterance

# Documentation: https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/custom-steps


@given('{light_name} has been set to {color}.')
@given('{light_name} is now {color}.')
@given('{light_name} was set to {color}.')
def given_set_color(context, light_name, color):
    # check to make sure things are in the proper state with MQTT
    pass
