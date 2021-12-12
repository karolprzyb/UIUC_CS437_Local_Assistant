# Documentation:
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/test-steps
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/scenario-outlines

Feature: turn-on-bulb
  Scenario: turn on bulb
    Given an English speaking user
    And a 2 minute timeout
     When the user says "<turn on prompts>"
     Then "mqtt-light-and-smartplug-control-skill" should reply with dialog from "turn.bulb.on.dialog"

   Examples: light bulb prompts  # Table heading
        | turn on prompts     |   # Column heading
        | Turn desk lamp on.  |   # First value
        | Turn on desk lamp.  |   # Second value
        | Activate desk lamp. |   # Third value