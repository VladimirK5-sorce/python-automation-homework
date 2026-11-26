import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """PageObject для страницы корзины покупок."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу корзины.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "inventory_item_name")

    @allure.step("Получить список названий товаров в корзине")
    def get_cart_items(self) -> list[str]:
        """
        Собирает и возвращает список названий всех товаров в корзине.

        :return: Список строк с названиями товаров.
        """
        items = self.driver.find_elements(*self.cart_items)
        return [item.text for item in items]

    @allure.step("Нажать кнопку оформления заказа (Checkout)")
    def click_checkout(self) -> None:
        """Нажимает кнопку Checkout для перехода к оформлению заказа."""
        self.driver.find_element(*self.checkout_button).click()
