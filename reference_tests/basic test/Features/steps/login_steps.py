from behave import given, when, then
from playwright.sync_api import sync_playwright
from behave.api.async_step import async_run_until_complete

#from models login_page import LoginPage

@given ('I navigate to login page')
def step_open_login_page(context): 
    #note adding the playwright here means that different scenarios cant run properly.
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context.browser = browser 
    context.page = browser.new_page()
    context.page.goto("http://uitestingplayground.com/sampleapp")

@when ('I enter a VALID username and a VALID password')
def step_enter_valid_credentials(context):
    context.page.locator('input[name="UserName"]').fill('Standard_User')
    context.page.locator('input[name="Password"]').fill('pwd')
    
@when ('I enter an VALID username and a INVALID password')
def step_enter_invalid_credentials(context):
    context.page.locator('input[name="UserName"]').fill('Standard_User')
    context.page.locator('input[name="Password"]').fill('ajkbs')

@when ('I click on the login button')
def step_press_login(context):
    context.page.click("#login")

@then ('I should verify that login was successful')
def step_verify_dashboard(context):
    assert "Welcome" in context.page.locator("#loginstatus").text_content()
    button_text = context.page.locator("#login").text_content().strip()
    assert "Log Out" in button_text

@then ('I should verify that login failed with Invalid username password error')
def step_verify_incorrect_credentials(context):
    assert "Invalid username/password" in context.page.locator("#loginstatus").text_content()
    button_text = context.page.locator("#login").text_content().strip()
    assert "Log In" in button_text
