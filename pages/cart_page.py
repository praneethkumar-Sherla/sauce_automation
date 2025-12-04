class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator("//div[@class='cart_item']")
        self.checkout_btn = page.locator("//button[@id='checkout']")

    def verify_items_present(self, expected_items):
        names_in_cart = [item.inner_text().strip()
        for item in self.cart_items.locator("//div[@class='inventory_item_name']").all()]
        print(f"Names in cart: {names_in_cart}")
        print(f"Expected items: {expected_items}")
        assert all(item in names_in_cart for item in expected_items), "Cart mismatch!"


    def checkout(self):
        self.checkout_btn.click()
