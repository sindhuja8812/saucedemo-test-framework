"""Page Object for the Sauce Demo cart screen."""


class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def checkout(self):
        self.checkout_button.click()
