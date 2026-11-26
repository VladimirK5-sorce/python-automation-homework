import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """PageObject для главной страницы каталога товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует главную страницу каталога.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Добавляет товар в корзину по его названию в каталоге.

        :param product_name: Полное название товара.
        """
        formatted_name = product_name.lower().replace(" ", "-")
        add_button = (By.ID, f"add-to-cart-{formatted_name}")
        self.driver.find_element(*add_button).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Нажимает на иконку корзины и переходит на её страницу."""
        self.driver.find_element(*self.cart_link).click()
