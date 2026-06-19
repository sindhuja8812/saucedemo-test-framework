"""
Cart test suite.

Covers basic functional flows for adding items and verifying the cart
badge / cart contents stay in sync. Uses the `logged_in_page` fixture
from conftest.py to skip repeating the login steps in every test.
"""
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_single_item_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    assert inventory.get_cart_count() == 1


def test_add_multiple_items_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.add_item_to_cart_by_name("Sauce Labs Bike Light")
    assert inventory.get_cart_count() == 2


def test_cart_page_reflects_added_item(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.open_cart()

    cart = CartPage(logged_in_page)
    assert cart.get_item_count() == 1
