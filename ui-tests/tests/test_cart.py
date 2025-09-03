from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_add_multiple_items_to_cart(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.add_product_to_cart("Sauce Labs Bike Light")

    assert inventory.get_cart_count() == "2"

    inventory.go_to_cart()
    cart = CartPage(driver)
    items = cart.get_cart_items()
    assert len(items) == 2
