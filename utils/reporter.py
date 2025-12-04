import allure
import datetime

class AllureReporter:

    def __init__(self, page):
        self.page = page

    def timestamp(self):
        """
        Generate a timestamp string in the format YYYYMMDD-HHMMSS.
            
        Returns:
            str: Timestamp string in the format YYYYMMDD-HHMMSS.
        """
        return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    def attach_screenshot(self, name="screenshot"):
        """
        Capture a full-page screenshot and attach it to the Allure report.
        
        Args:
            name (str, optional): Name for the screenshot attachment. Defaults to "screenshot".
            
        Raises:
            Exception: If screenshot capture fails or Allure attachment fails.
        """
        screenshot = self.page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG,
            extension="png"
        )
        print(f"[SCREENSHOT] Captured : {name}")

    def step(self, description: str):
        """
        Add a step description to the Allure test report.
        
        Args:
            description (str): Description of the test step to be added to the report.
            
        Raises:
            Exception: If Allure dynamic description setting fails.
        """
        allure.dynamic.description(f"Step: {description}")
        print(f"[Allure Step] : {description}")
