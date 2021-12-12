# Documentation:
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/test-steps
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/scenario-outlines

Feature: turn-off-plug
  Scenario: turn off plug
    Given an English speaking user
    And a 2 minute timeout
     When the user says "<turn off prompts>"
     Then "mqtt-light-and-smartplug-control-skill" should reply with dialog from "turn.plug.off.dialog"

   Examples: plug prompts  # Table heading
        | turn off prompts         |   # Column heading
        | Turn coffee maker off.   |   # First value
        | Turn off coffee maker.   |   # Second value
        | Deactivate coffee maker. |   # Third value