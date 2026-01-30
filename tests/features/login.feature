Feature: Verify Login

  Scenario: Verify user is able to login with valid credentials
    Given I navigate to login page
    When I enter VALID username: "user1" and VALID password: "pwd"
    When I click on the login button 
    Then I should verify that loginstatus shows: "Welcome"
    Then I should verify that loginstatus shows: "user1"
    Then I should verify that the button updates to show: "Log Out"

  Scenario: Verify that a user will fail to login with invalid credentials 
    Given I navigate to login page
    When I enter VALID username "username" and INVALID password "shdskd"
    When I click on the login button
    Then I should verify that loginstatus shows: "Invalid username/password"
    Then I should verify that the button updates to show: "Log In"  