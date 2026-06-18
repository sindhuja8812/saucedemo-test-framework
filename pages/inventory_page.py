"""Page Object for the Sauce Demo inventory (product listing) screen."""


class InventoryPage:
    PATH = "inventory.html"

    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_item_to_cart_by_name(self, item_name: str):
        item = self.page.locator(".inventory_item", has_text=item_name)
        item.locator("button", has_text="Add to cart").click()

    def get_cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.inner_text())

    def open_cart(self):
        self.cart_link.click()
