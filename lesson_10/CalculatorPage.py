import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """PageObject для работы со страницей медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу калькулятора.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium"
            "-webdriver-java/slow-calculator.html"
        )
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get(self.url)

    @allure.step("Установить задержку вычислений: {seconds} сек.")
    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает время задержки вывода результата в секундах.

        :param seconds: Время ожидания в секундах.
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажать кнопку калькулятора '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку калькулятора по её тексту.

        :param button_text: Текст на кнопке (цифра или оператор).
        """
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()

    @allure.step("Дождаться результата '{expected_result}' на экране")
    def get_result(self, expected_result: str, timeout: int = 50) -> str:
        """
        Ожидает появления заданного текста на экране и возвращает его.

        :param expected_result: Ожидаемое значение на экране.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Текст результата с экрана калькулятора.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.screen, str(expected_result)
            )
        )
        return self.driver.find_element(*self.screen).text
