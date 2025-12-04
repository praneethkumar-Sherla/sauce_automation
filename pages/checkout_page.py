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
        """
        Fill in checkout information and proceed to the next step.
        
        Args:
            first (str, optional): First name for checkout. Defaults to "Praneeth".
            last (str, optional): Last name for checkout. Defaults to "Kumar".
            zip_code (str, optional): ZIP/postal code for checkout. Defaults to "56789".
            
        Raises:
            TimeoutError: If form fields are not visible or finish button does not appear after submission.
            Exception: If form filling or submission fails.
        """
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip_code)
        self.continue_btn.click()
        # Wait for the checkout step two page to load
        self.finish_btn.wait_for(state="visible", timeout=10000)

    def finish_checkout(self):
        """
        Complete the checkout process by clicking the finish button.
            
        Raises:
            TimeoutError: If the finish button is not visible within the timeout period.
            Exception: If button click fails.
        """
        self.finish_btn.first.wait_for(state="visible")
        self.finish_btn.click()

    def assert_checkout_complete(self):
        """
        Assert that the checkout was completed successfully by verifying the completion message.
            
        Raises:
            AssertionError: If the completion message does not match the expected text.
            Exception: If the completion header element cannot be retrieved.
        """
        msg = self.complete_header.inner_text()
        assert msg == "Thank you for your order!", "Checkout completion failed!"
