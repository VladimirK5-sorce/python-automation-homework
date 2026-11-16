from selenium import webdriver
from CalculatorPage import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.set_delay(45)

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result_text = calc_page.get_result("15", timeout=50)
    driver.quit()

    assert result_text == "15", (
        f"Ожидался результат '15', но получили '{result_text}'"
    )
