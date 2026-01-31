Feature: Verify Login

  Background:
    Given I navigate to login page

  Scenario Outline: Verify user is able to login with valid credentials
    Given I enter VALID username: "<username>" and password: "pwd"
    When I click on the login button 
    Then I should verify that loginstatus shows: "Welcome"
    Then I should verify that loginstatus shows: "<username>"
    Then I should verify that the button updates to show: "Log Out"

    Examples: These are valid Usernames. The only valid password is pwd
    | username |
    | u        |
    | uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu  |
    | !57@#$%^&*()_+-=`~/*-.  |

  Scenario Outline: Verify that a user will fail to login with invalid credentials 
    Given I enter INVALID username "<username>" and password "<password>"
    When I click on the login button
    Then I should verify that loginstatus shows: "Invalid username/password"
    Then I should verify that the button updates to show: "Log In"  

    #Note: the 'empty' fields are simply not filled 
    Examples: These are Invalid username/password combinations. 
    | username  | password     |
    | empty     | pwd          |
    | user1     | ioweidjbhk   |
    | user1     | empty        |

