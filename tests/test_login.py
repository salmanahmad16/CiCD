import time

import pytest
from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("Admin", "admin123")
    time.sleep(2)
    assert "OrangeHRM" in driver.title


# def test_invalid_login(driver):
#     login_page = LoginPage(driver)
#     login_page.load()
#     login_page.login("Salman", "123455")
#     error = login_page.error_message()
#     assert "Invalid credentials" in error