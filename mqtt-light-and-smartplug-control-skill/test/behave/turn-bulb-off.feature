# Documentation:
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/test-steps
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/scenario-outlines

Feature: turn-off-bulb
  Scenario: turn off bulb
    Given an English speaking user
    And a 2 minute timeout
     When the user says "<turn off prompts>"
     Then "mqtt-light-and-smartplug-control-skill" should reply with dialog from "turn.bulb.off.dialog"

   Examples: light bulb prompts  # Table heading
        | turn off prompts      |   # Column heading
        | Turn desk lamp off.   |   # First value
        | Turn off desk lamp.   |   # Second value
        | Deactivate desk lamp. |   # Third value