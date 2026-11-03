from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        # 1. Открываем страницу задания
        url = "https://the-internet.herokuapp.com/dynamic_loading/2"
        driver.get(url)

        # 2. Находим и нажимаем на кнопку Start
        start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_button.click()

        # 3. Явное ожидание появления текста Hello World! (максимум 10 секунд)
        finish_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        # 4. Делаем скриншот страницы в папку урока
        driver.save_screenshot("lesson_06/screenshot_task1.png")

        # 5. Проверяем, что появившийся текст равен "Hello World!"
        actual_text = finish_element.text
        assert actual_text == "Hello World!", (
            f"Ожидался текст 'Hello World!', но получен '{actual_text}'"
        )
    finally:
        driver.quit()
