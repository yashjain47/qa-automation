from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_user_info("John", "Doe", "12345")
    # Overview page should show totals
    assert "checkout-step-two" in driver.current_url

    checkout.finish_checkout()
    assert "Checkout: Complete!" in checkout.get_confirmation_message()
