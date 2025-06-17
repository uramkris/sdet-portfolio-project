import pytest
from pages.login_page import LoginPage

# To run: `pytest tests/test_login.py`

def test_successful_login(driver):
    """
    User Story: As a user, I want to log in successfully.
    """
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Assertion: Verify that the URL changed to the inventory page
    assert "inventory.html" in login_page.get_url(), "Login failed or redirected to wrong page."

def test_invalid_login(driver):
    """
    User Story: As a user, I should see an error message for invalid credentials.
    """
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    # Assertion: Verify the error message is displayed and correct
    error_msg = login_page.get_error_message()
    assert "Epic sadface: Sorry, this user has been locked out." in error_msg
