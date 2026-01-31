    # The Purpose for this test it to verify that Playwright will only click buttons after they stop moving. 
    # For example, for locator.click(), Playwright will ensure that:
        # locator resolves to exactly one element
        # element is Visible
        # element is Stable, as in not animating or completed animation
        # element Receives Events, as in not obscured by other elements
        # element is Enabled


Feature: Verify Animation Page

  Scenario: Verify that we can start the moving button animation and then click on it as it moves
    Given I navigate to page with the moving button
    When I click Start Animation  
    When I wait for the button to stop moving and then click it
    Then I should verify that the button was pressed

