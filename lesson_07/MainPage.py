from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self, product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        add_button = (By.ID, f"add-to-cart-{formatted_name}")
        self.driver.find_element(*add_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
