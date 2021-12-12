# Documentation:
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/test-steps
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/scenario-outlines

Feature: set-bulb-color
  Scenario: set bulb color
    Given an English speaking user
    And a 2 minute timeout
     When the user says "<color prompts>"
     Then "mqtt-light-and-smartplug-control-skill" should reply with dialog from "set.bulb.color.dialog"

   Examples: light bulb prompts  # Table heading
        | color prompts                         |   # Column heading
        | Change the color of desk lamp to red. |   # First value
        | Set desk lamp to red.                 |   # Second value
        | Change desk lamp to red.              |   # Third value
        | Set desk lamp's color to red.         |