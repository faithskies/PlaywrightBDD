Feature: Verify Login

  Scenario: Verify user is able to login with valid credentials
    Given I navigate to login page
    When I enter a VALID username and a VALID password
    When I click on the login button 
    Then I should verify that login was successful

  Scenario: Verify that a user will fail to login with invalid credentials 
    Given I navigate to login page
    When I enter an VALID username and a INVALID password
    When I click on the login button
    Then I should verify that login failed with Invalid username password error 