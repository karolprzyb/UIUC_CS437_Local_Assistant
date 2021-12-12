# Documentation:
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/test-steps
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/scenario-outlines

Feature: set-bulb-dimness
  Scenario: set bulb dimness
    Given an English speaking user
    And a 2 minute timeout
     When the user says "<dimness prompts>"
     Then "mqtt-light-and-smartplug-control-skill" should reply with dialog from "set.bulb.dimness.dialog"

   Examples: light bulb prompts  # Table heading
        | dimness prompts                                |   # Column heading
        | Dim desk lamp to 67 percent.                   |   # First value
        | Set desk lamp to 67 percent.                   |   # Second value
        | Set the dimness of desk lamp to 67 percent.    |   # Third value
        | Set the brightness of desk lamp to 67 percent. |
        | Increase desk lamp brightness to 67 percent.   |
        | Decrease desk lamp brightness to 67 percent.   |