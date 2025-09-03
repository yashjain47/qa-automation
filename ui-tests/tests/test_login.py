import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_loaded()
    assert len(driver.find_elements(*inventory.inventory_items)) > 0

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.load()
    login.login("locked_out_user", "secret_sauce")

    assert "locked out" in login.get_error_message().lower()