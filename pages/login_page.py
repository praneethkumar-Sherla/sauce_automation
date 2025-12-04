class LoginPage:
    """Page Object Model for the Sauce Demo login page."""
    
    def __init__(self, page):
        """
        Initialize the LoginPage with a Playwright page object.
        
        Args:
            page: Playwright page object for browser interaction.
        """
        self.page = page
        self.username = page.locator("//input[@id='user-name']")
        self.password = page.locator("//input[@id='password']")
        self.login_btn = page.locator("//input[@id='login-button']")

    def login(self, user="standard_user", pwd="secret_sauce"):
        """
        Navigate to Sauce Demo and perform login with provided credentials.
        
        Args:
            user (str, optional): Username for login. Defaults to "standard_user".
            pwd (str, optional): Password for login. Defaults to "secret_sauce".
            
        Raises:
            TimeoutError: If the page elements do not become visible within the timeout period.
            Exception: If navigation fails or element interaction fails.
        """
        self.page.goto("https://www.saucedemo.com/")
        self.page.locator("text=Swag Labs").first.wait_for(state="visible", timeout=10000)
        self.username.wait_for(state="visible", timeout=10000)
        self.password.wait_for(state="visible", timeout=10000)
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
