import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """PageObject для страницы оформления заказа и расчёта стоимости."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу оформления заказа.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить форму данных покупателя: {first_name} {last_name}")
    def fill_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет поля имени, фамилии и индекса и переходит к итогу.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый индекс.
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(
            postal_code
        )
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую стоимость заказа")
    def get_total_price(self) -> str:
        """
        Считывает итоговую сумму заказа со страницы и убирает префикс.

        :return: Итоговая сумма заказа в виде строки (например, '$58.29').
        """
        total_text = self.driver.find_element(*self.total_label).text
        return total_text.replace("Total: ", "")
