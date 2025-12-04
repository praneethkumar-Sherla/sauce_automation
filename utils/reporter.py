import allure
import datetime

class AllureReporter:

    def __init__(self, page):
        self.page = page

    def timestamp(self):
        return datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    def attach_screenshot(self, name="screenshot"):
        screenshot = self.page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG,
            extension="png"
        )
        print(f"[SCREENSHOT] Captured : {name}")

    def step(self, description: str):
        allure.dynamic.description(f"Step: {description}")
        print(f"[Allure Step] : {description}")
