    # A web application may use a progress bar to reflect state of some lengthy process. Thus a test may need to read the value of a progress bar to determine if it is time to proceed or not.
    # Create a test that clicks Start button and then waits for the progress bar to reach 75%. Then the test should click Stop. The less the differnce between value of the stopped progress bar and 75% the better your result.

# of note, this one was tricky because I found that await expect was a little too slow for this scenario so instead I used a loop to check every half second

Feature: Verify Progress Bar Page

  Background:
    Given I navigate to page with the progress bar

  Scenario: Click on the stop button when it reaches 75%
    Given I click Start button to start the progress bar  
    When I wait for the progress bar to reach "75" and click Stop
    Then I should verify that we clicked stop at the correct time
