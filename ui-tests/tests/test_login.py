import pytest
from pages.login_page import LoginPage

def test_successful_login(driver):
    page = LoginPage(driver)
    page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.login("locked_out_user", "secret_sauce")
    assert "Epic sadface" in driver.page_source
