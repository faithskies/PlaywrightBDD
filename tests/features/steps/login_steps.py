from behave import given, when, then
from playwright.sync_api import sync_playwright, expect
from behave.api.async_step import async_run_until_complete

# import pages that include locators 
from pages.login_page import LoginPage

@given ('I navigate to login page')
@async_run_until_complete
async def step_open_login_page(context): 
    login_page = LoginPage(context.page)
    await login_page.navigate()

@when ('I enter VALID username: "{username}" and VALID password: "{password}"')
@async_run_until_complete
async def step_enter_valid_credentials(context, username:str, password:str):
    login_page = LoginPage(context.page)
    await login_page.fill_form_field(username, password)
    
@when ('I enter VALID username "{username}" and INVALID password "{password}"')
@async_run_until_complete
async def step_enter_invalid_credentials(context, username:str, password:str):
    login_page = LoginPage(context.page)
    await login_page.fill_form_field(username, password)

@when ('I click on the login button')
@async_run_until_complete
async def step_press_login(context):
    # context.page.click("#login")
    login_page = LoginPage(context.page)
    await login_page.submit_login()

@then ('I should verify that loginstatus shows: "{message}"')
@async_run_until_complete
async def step_verify_dashboard(context, message:str):
    login_page = LoginPage(context.page)
    
    resultFound = await login_page.verify_loginstatus(message)
    assert resultFound, f"Expected login status to contain '{message}'"

@then ('I should verify that the button updates to show: "{text}"')
@async_run_until_complete
async def step_verify_button_text(context, text:str):
    login_page = LoginPage(context.page)
    
    resultFound = await login_page.verify_buttonstatus(text)
    assert resultFound, f"Expected Button to show '{text}'"
    
    # button_text = login_page.submit.text_content().strip()
    # assert text in button_text
