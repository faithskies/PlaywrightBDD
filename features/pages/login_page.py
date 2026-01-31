from playwright.async_api import Page
from pages.base_page import BasePage 

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
        
    # fills the username and password fields with specified example texts    
    async def fill_form_field(self, username, password):
        #checks for if the username or password is 'empty' then it skips filling the field.  
        if username != 'empty':
            await self.username_field.fill(username)
        if password != 'empty':
            await self.password_field.fill (password)
    
    # checks if the expected text exists within the loginstatus feild   
    async def verify_loginstatus(self, temptext):  
        actual_text = await self.loginstatus.inner_text()
        if temptext in actual_text:
            return True
        else:
            return False
    
    #checks to see the text of the login button    
    async def verify_buttonstatus(self, temptext):  
        actual_text = await self.submit.inner_text()
        if temptext in actual_text:
            return True
        else:
            return False
