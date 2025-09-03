from ui_tests.pages.login_page import LoginPage

def test_end_to_end(driver):
    # Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Add to cart
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("id", "add-to-cart-sauce-labs-bike-light").click()

    # Checkout process (simplified)
    driver.find_element("class name", "shopping_cart_link").click()
    driver.find_element("id", "checkout").click()
    driver.find_element("id", "first-name").send_keys("John")
    driver.find_element("id", "last-name").send_keys("Doe")
    driver.find_element("id", "postal-code").send_keys("12345")
    driver.find_element("id", "continue").click()
    driver.find_element("id", "finish").click()

    assert "Thank you for your order!" in driver.page_source
