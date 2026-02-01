from playwright.async_api import Page, expect
from pages.base_page import BasePage 
import re # used for when_percent_reached(self, percent): 
import asyncio

class ProgressBarPage(BasePage):
    def __init__(self, page: Page): 
        super().__init__(page)
        self.start_button = page.locator("#startButton")
        self.stop_button = page.locator("#stopButton")
        self.progress_bar = page.locator("#progressBar")
        self.result = page.locator("#result")
        
    async def navigate(self):
        await self.page.goto("http://uitestingplayground.com/progressbar", timeout=5000)
         
    async def click_start(self):
         await self.start_button.click()    

    # I went with this method over the await expect becuase I could dial in exactly how often I want it to check allowing for a more accurate result. 
    # In most cases I imagine that the timing doesnt matter as much but it does in this case. 
    async def when_percent_reached(self, percent):
        for i in range(100):  # 0..39 → 40 iterations
            current_percent = await self.progress_bar.inner_text()
            if current_percent >= percent:
                await self.stop_button.click()
                print("percent is", percent, "current_percent is", current_percent)
                return  # exit as soon as we reach the target
            await asyncio.sleep(.5)  # wait 1 second
        await self.stop_button.click()
            
    # # This is another way of doing this.. however I found that the await expect only checks every few seconds and often is way too late
    # async def when_percent_reached(self, percent):  
    #     #await expect(locator).toContainText()
    #     await expect(self.progress_bar).to_contain_text(re.compile(r"7[5-9]|8[0-9]|9[0-9]|100"),timeout=40000)
    #     #await expect(self.progress_bar).to_contain_text(["75%", "76%", "77%", "78%", "79%", "80%", "81%", "82%", "83%", "84%", "85%", "86%", "87%", "88%", "89%", "100%"],timeout=40000)
    #     #await expect(self.progress_bar).to_contain_text(percent,timeout=40000)
    #     await self.stop_button.click() 
    
    async def determine_result(self):
     
        await expect(self.result).to_contain_text("Result:")
        result = await self.result.inner_text()
        # remove the text we dont need. example: Result: -9, duration: 6558
        print("result is", result)
        part = result.split("Result: ")[1] 
        result = part.split(", duration")[0]
        return int(result)
        
    