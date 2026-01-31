from behave import given, when, then
from playwright.sync_api import sync_playwright, expect
from behave.api.async_step import async_run_until_complete

# import pages that include locators 
from pages.animation_page import AnimationPage

@given ('I navigate to page with the moving button')
@async_run_until_complete
async def step_open_login_page(context): 
    animation_page = AnimationPage(context.page)
    await animation_page.navigate()


@when ('I click Start Animation')
@async_run_until_complete
async def step_press_login(context):
    animation_page = AnimationPage(context.page)
    await animation_page.start_animation()
    
@when ('I wait for the button to stop moving and then click it')
@async_run_until_complete
async def click_moving_target(context):
    animation_page = AnimationPage(context.page)
    await animation_page.click_moving_target()

@then ('I should verify that the button was pressed')
@async_run_until_complete
async def step_verify_dashboard(context):
    animation_page = AnimationPage(context.page)
    
    resultFound = await animation_page.verify_action_status()
    assert resultFound, f"Expected status to report the button was pressed"