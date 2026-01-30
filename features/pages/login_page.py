from playwright.async_api import Page
from base_page import BasePage 

class LoginPage(BasePage):
    def __init__(self, page: Page): 
        super().__init__(page)
        self.username_field = page.locator('input[name="UserName"]')
        self.password_field = page.locator('input[name="Password"]')
        self.submit = page.locator("#login")
        self.loginstatus = page.locator("#loginstatus")
        
    async def navigate(self):
        await self.page.goto("http://uitestingplayground.com/sampleapp", timeout=5000)
         
    async def submit_login(self):
        await self.submit.click()    
        
    async def fill_form_field(self, username, password):
        await self.username_field.fill(username)
        await self.password_field.fill (password)
        
    async def verify_loginstatus(self, temptext):  
        actual_text = await self.loginstatus.inner_text()
        if temptext in actual_text:
            return True
        else:
            return False
        
    async def verify_buttonstatus(self, temptext):  
        actual_text = await self.submit.inner_text()
        if temptext in actual_text:
            return True
        else:
            return False
