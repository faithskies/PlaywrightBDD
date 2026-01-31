from playwright.async_api import Page
from pages.base_page import BasePage 

class AnimationPage(BasePage):
    def __init__(self, page: Page): 
        super().__init__(page)
        self.start_animation_button = page.locator("#animationButton")
        self.moving_target_button = page.locator("#movingTarget")
        self.action_status = page.locator("#opstatus")
        
    async def navigate(self):
        await self.page.goto("http://uitestingplayground.com/animation", timeout=5000)
         
    async def start_animation(self):
         await self.start_animation_button.click()    
    
    async def click_moving_target(self):
         await self.moving_target_button.click()  
    
    async def verify_action_status(self):  
        actual_text = await self.action_status.inner_text()
        if "Moving Target clicked" in actual_text:
            return True
        else:
            return False    
    
        