from behave import given, when, then
from playwright.sync_api import sync_playwright, expect
from behave.api.async_step import async_run_until_complete

# import pages that include locators 
from pages.progress_bar_page import ProgressBarPage

@given ('I navigate to page with the progress bar')
@async_run_until_complete
async def step_open_page(context): 
    bar_page = ProgressBarPage(context.page)
    await bar_page.navigate()

@given ('I click Start button to start the progress bar')
@async_run_until_complete
async def step_click_start(context):
    bar_page = ProgressBarPage(context.page)
    await bar_page.click_start()
    
@when ('I wait for the progress bar to reach "{percent}" and click Stop')
@async_run_until_complete
async def step_wait_and_press_start(context, percent:int):
    bar_page = ProgressBarPage(context.page)
    await bar_page.when_percent_reached(percent)

@then ('I should verify that we clicked stop at the correct time')
@async_run_until_complete
async def step_verify_score(context):
    bar_page = ProgressBarPage(context.page)
    result = await bar_page.determine_result()
    #I chose an arbitrary number that I hope to beat. 
    assert result < 10, f"Result too high: {result}"