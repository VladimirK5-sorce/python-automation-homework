import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_fill_form():
    
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    
    
    wait = WebDriverWait(driver, 10)
    
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html ")
    
    
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    
    
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    
    
    zip_code_field = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле Zip code должно быть красным!"
    
    
    
    green_fields_ids = [
        "first-name", "last-name", "address", "e-mail", 
        "phone", "city", "country", "job-position", "company"
    ]
    
    for field_id in green_fields_ids:
        field = driver.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), f"Поле {field_id} не подсвечено зеленым!"
        
    
    driver.quit()
