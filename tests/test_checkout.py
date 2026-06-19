"""
Checkout test suite.

Test cases derived from a decision table on the three checkout-info
fields (first name / last name / postal code) being present or
missing. See docs/test_design_rtm.md for the full decision table.
"""
import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

CHECKOUT_CASES = [
    pytest.param("Sindhuja", "K", "600001", True, id="TC06_all_fields_present"),
    pytest.param("", "K", "600001", False, id="TC07_missing_first_name"),
    pytest.param("Sindhuja", "", "600001", False, id="TC08_missing_last_name"),
    pytest.param("Sindhuja", "K", "", False, id="TC09_missing_postal_code"),
]


@pytest.mark.parametrize("first, last, postal, should_succeed", CHECKOUT_CASES)
def test_checkout_form_validation(logged_in_page, first, last, postal, should_succeed):
    inventory = InventoryPage(logged_in_page)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.open_cart()

    cart = CartPage(logged_in_page)
    cart.checkout()

    checkout = CheckoutPage(logged_in_page)
    checkout.fill_info(first, last, postal)

    if should_succeed:
        assert "Overview" in checkout.get_page_title()
    else:
        assert checkout.error_message.is_visible()
