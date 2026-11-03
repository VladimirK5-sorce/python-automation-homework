from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        url = "https://the-internet.herokuapp.com/dynamic_loading/2"
        driver.get(url)

        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        finish_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        driver.save_screenshot("lesson_06/screenshot_task1.png")

        actual_text = finish_element.text
        assert actual_text == "Hello World!", (
            f"Ожидался текст 'Hello World!', но получен '{actual_text}'"
        )
    finally:
        driver.quit()
