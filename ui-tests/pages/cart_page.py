from time import sleep
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.checkout_button = (By.ID, "checkout")

    def get_cart_items(self):
        return self.driver.find_elements(*self.cart_items)

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        sleep(1)
