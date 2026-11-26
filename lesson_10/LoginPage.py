import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """PageObject для страницы авторизации интернет-магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует страницу авторизации.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.url = "https://saucedemo.com"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу авторизации магазина")
    def open(self) -> None:
        """Открывает главную страницу входа в магазин."""
        self.driver.get(self.url)

    @allure.step("Авторизоваться под пользователем '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему с указанными логином и паролем.

        :param username: Имя пользователя (логин).
        :param password: Пароль пользователя.
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
