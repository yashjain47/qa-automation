import sys
sys.path.append("../ui-tests/")
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_end_to_end(driver):
    # Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_loaded()

    # Add to cart
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.add_product_to_cart("Sauce Labs Bike Light")
    assert inventory.get_cart_count() == "2"

    # Go to Cart
    inventory.go_to_cart()
    cart = CartPage(driver)
    assert len(cart.get_cart_items()) == 2
    cart.proceed_to_checkout()

    # Checkout with details
    checkout = CheckoutPage(driver)
    checkout.fill_user_info("John", "Doe", "12345")

    # Confirmation
    assert "checkout-step-two" in driver.current_url
    items = driver.find_elements("class name", "cart_item")
    assert len(items) == 2
    summary_total = driver.find_element("class name", "summary_total_label").text
    assert "Total:" in summary_total

    # Finish Checkout
    checkout.finish_checkout()

    # Finish Confirmation
    confirmation = checkout.get_confirmation_message()
    assert "Checkout: Complete!" in confirmation

    driver.find_element("id", "back-to-products").click()
    assert inventory.is_loaded()



