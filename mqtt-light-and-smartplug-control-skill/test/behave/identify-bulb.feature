# Documentation:
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/test-steps
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/scenario-outlines

Feature: identify-bulb
  Scenario: identify which bulb has the provided name
    Given an English speaking user
    And a 2 minute timeout
     When the user says "<identify prompts>"
     Then "mqtt-light-and-smartplug-control-skill" should reply with dialog from "identify.bulb.dialog"

   Examples: light bulb prompts  # Table heading
        | identify prompts                 |   # Column heading
        | Identify desk lamp.              |   # First value
        | Which bulb is desk lamp?         |   # Second value
        | Show me which bulb is desk lamp. |   # Third value
        | Make desk lamp blink.            |
        | Make desk lamp flash.            |
        | Blink desk lamp.                 |
        | Flash desk lamp.                 |