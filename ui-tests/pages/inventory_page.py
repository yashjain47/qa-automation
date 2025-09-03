from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.products_title = (By.CLASS_NAME, "title")
        self.inventory_items = (By.CLASS_NAME, "inventory_item")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")

    def is_loaded(self):
        return "inventory" in self.driver.current_url and \
               self.driver.find_element(*self.products_title).is_displayed()

    def add_product_to_cart(self, product_name):
        button = self.driver.find_element(By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        button.click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def sort_by_price_low_to_high(self):
        from selenium.webdriver.support.ui import Select
        Select(self.driver.find_element(*self.sort_dropdown)).select_by_value("lohi")

    def get_product_prices(self):
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(p.text.replace("$", "")) for p in prices]


# driver = webdriver.Chrome()
# login = LoginPage(driver)
# login.load()
# login.login("locked_out_user", "secret_sauce")
# sleep(5)