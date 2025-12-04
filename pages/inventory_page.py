import random

class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.item_cards = page.locator("//div[@class='inventory_item']")
        self.shopping_cart_link = page.locator("//a[@class='shopping_cart_link']")

    def get_random_items(self, count=3):
        """
        Get random indices of items from the inventory page.
        
        Args:
            count (int, optional): Number of random items to select. Defaults to 3.
            
        Returns:
            list[int]: List of random indices representing item positions.
            
        Raises:
            ValueError: If count is greater than the total number of available items.
        """
        total_items = self.item_cards.count()
        indices = random.sample(range(total_items), count)
        return indices

    def add_items_to_cart(self, indices):
        """
        Add items to the shopping cart by their indices and return their names.
        
        Args:
            indices (list[int]): List of item indices to add to the cart.
            
        Returns:
            list[str]: List of names of items that were added to the cart.
            
        Raises:
            IndexError: If any index in indices is out of range for available items.
            Exception: If element interaction fails (e.g., button not clickable).
        """
        added_item_names = []
        for idx in indices:
            item = self.item_cards.nth(idx)
            name = item.locator("//div[@class='inventory_item_name ']").inner_text()
            item.locator("//button").click()
            added_item_names.append(name)
        return added_item_names

    def go_to_cart(self):
        """
        Navigate to the shopping cart page by clicking the cart link.
            
        Raises:
            TimeoutError: If the shopping cart link is not visible or clickable.
            Exception: If navigation fails.
        """
        self.shopping_cart_link.click()
