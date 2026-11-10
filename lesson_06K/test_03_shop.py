import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

def test_saucedemo_shop():
    
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    
    driver.get("https://www.saucedemo.com/")
    
    
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()
    
    
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    
    
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    
    
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    
    
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("123456")
    
    
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    
    
    total_element = driver.find_element(By.CSS_SELECTOR, ".summary_total_label")
    total_text = total_element.text  # Получим строку вида "Total: $58.29"
    
    
    driver.quit()
    

    assert total_text == "Total: $58.29", f"Ожидалась сумма 'Total: $58.29', но получили '{total_text}'"
