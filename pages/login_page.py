class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("//input[@id='user-name']")
        self.password = page.locator("//input[@id='password']")
        self.login_btn = page.locator("//input[@id='login-button']")

    def login(self, user="standard_user", pwd="secret_sauce"):
        self.page.goto("https://www.saucedemo.com/")
        self.page.locator("text=Swag Labs").first.wait_for(state="visible", timeout=10000)
        self.username.wait_for(state="visible", timeout=10000)
        self.password.wait_for(state="visible", timeout=10000)
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
