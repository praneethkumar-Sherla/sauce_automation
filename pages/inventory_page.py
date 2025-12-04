import random

class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.item_cards = page.locator("//div[@class='inventory_item']")
        self.shopping_cart_link = page.locator("//a[@class='shopping_cart_link']")

    def get_random_items(self, count=3):
        total_items = self.item_cards.count()
        indices = random.sample(range(total_items), count)
        return indices

    def add_items_to_cart(self, indices):
        added_item_names = []
        for idx in indices:
            item = self.item_cards.nth(idx)
            name = item.locator("//div[@class='inventory_item_name ']").inner_text()
            item.locator("//button").click()
            added_item_names.append(name)
        return added_item_names

    def go_to_cart(self):
        self.shopping_cart_link.click()
