# Documentation:
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/test-steps
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/scenario-outlines

Feature: turn-on-plug
  Scenario: turn on plug
    Given an English speaking user
    And a 2 minute timeout
     When the user says "<turn on prompts>"
     Then "mqtt-light-and-smartplug-control-skill" should reply with dialog from "turn.plug.on.dialog"

   Examples: plug prompts  # Table heading
        | turn on prompts        |   # Column heading
        | Turn coffee maker on.  |   # First value
        | Turn on coffee maker.  |   # Second value
        | Activate coffee maker. |   # Third value