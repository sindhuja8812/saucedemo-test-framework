"""
Login test suite.

Test cases below were derived using equivalence partitioning on the
(username, password) input pair, plus one boundary case for empty
input and one negative case specific to Sauce Demo's locked-out
account behaviour. See docs/test_design_rtm.md for the full mapping
back to requirements.
"""
import pytest
from pages.login_page import LoginPage

LOGIN_CASES = [
    pytest.param("standard_user", "secret_sauce", True, id="TC01_valid_login"),
    pytest.param("invalid_user", "secret_sauce", False, id="TC02_invalid_username"),
    pytest.param("standard_user", "wrong_password", False, id="TC03_invalid_password"),
    pytest.param("", "", False, id="TC04_empty_credentials"),
    pytest.param("locked_out_user", "secret_sauce", False, id="TC05_locked_out_account"),
]


@pytest.mark.parametrize("username, password, should_succeed", LOGIN_CASES)
def test_login_scenarios(page, username, password, should_succeed):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(username, password)

    if should_succeed:
        page.wait_for_url("**/inventory.html")
        assert "inventory.html" in page.url
    else:
        assert login_page.error_message.is_visible()
