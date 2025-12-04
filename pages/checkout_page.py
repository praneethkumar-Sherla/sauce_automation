class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("//input[@id='first-name']")
        self.last_name = page.locator("//input[@id='last-name']")
        self.zip_code = page.locator("//input[@id='postal-code']")
        self.continue_btn = page.locator("//input[@id='continue']")
        self.finish_btn = page.locator("//button[@id='finish']")
        self.complete_header = page.locator("//h2[@class='complete-header']")

    def fill_information(self, first="Praneeth", last="Kumar", zip_code="56789"):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip_code)
        self.continue_btn.click()
        # Wait for the checkout step two page to load
        self.finish_btn.wait_for(state="visible", timeout=10000)

    def finish_checkout(self):
        self.finish_btn.first.wait_for(state="visible")
        self.finish_btn.click()

    def assert_checkout_complete(self):
        msg = self.complete_header.inner_text()
        assert msg == "Thank you for your order!", "Checkout completion failed!"
