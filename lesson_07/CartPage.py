from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items(self):
        items = self.driver.find_elements(*self.cart_items)
        return [item.text for item in items]

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
