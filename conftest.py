import os
import sys

# Make sure `pages` is importable regardless of where pytest is invoked from
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest
from pages.login_page import LoginPage

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture
def logged_in_page(page):
    """Returns a page that's already logged in as the standard user.

    Use this fixture for any test that needs to start past the login
    screen (cart, checkout, sorting, etc.) so each test doesn't repeat
    the same login steps.
    """
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    page.wait_for_url("**/inventory.html")
    return page
