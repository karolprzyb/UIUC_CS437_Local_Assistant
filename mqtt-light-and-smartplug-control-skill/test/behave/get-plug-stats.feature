# Documentation:
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/test-steps
# https://mycroft-ai.gitbook.io/docs/skill-development/voight-kampff/scenario-outlines

Feature: plug-stats
  Scenario: provide energy use statistics for a plug
    Given an English speaking user
    And a 2 minute timeout
     When the user says "<plug stat prompts>"
     Then "mqtt-light-and-smartplug-control-skill" should reply with dialog from "get.plug.stats.dialog"

   Examples: plug prompts  # Table heading
        | stats prompts                                   |   # Column heading
        | Give me the energy usage of coffee maker.       |   # First value
        | Give me the energy statistics of coffee maker.  |   # Second value
        | Give me the energy stats of coffee maker.       |   # Third value
        | What are the energy statistics of coffee maker? |
        | What are the energy stats of coffee maker?      |
        | What is the energy usage of coffee maker?       |
        | How much energy is coffee maker using?          |