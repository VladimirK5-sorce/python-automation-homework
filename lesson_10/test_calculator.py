import allure
import pytest
from selenium import webdriver
from lesson_10.CalculatorPage import CalculatorPage


@pytest.fixture
def chrome_driver():
    """Создаёт и закрывает драйвер Chrome для теста калькулятора."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Калькулятор")
@allure.title("Проверка сложения чисел с задержкой 45 секунд")
@allure.description(
    "Открывает страницу медленного калькулятора, задаёт задержку 45 секунд, "
    "выполняет операцию 7 + 8 и проверяет отображение результата 15."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(chrome_driver) -> None:
    calc_page = CalculatorPage(chrome_driver)

    calc_page.open()
    calc_page.set_delay(45)

    with allure.step("Ввести выражение 7 + 8 ="):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    result_text = calc_page.get_result("15", timeout=50)

    with allure.step("Проверить, что результат на экране равен '15'"):
        assert result_text == "15", (
            f"Ожидался результат '15', но получили '{result_text}'"
        )
