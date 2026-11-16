from selenium import webdriver
from LoginPage import LoginPage
from MainPage import MainPage
from CartPage import CartPage
from CheckoutPage import CheckoutPage


def test_shop_purchase():
    driver = webdriver.Firefox()
    driver.maximize_window()

    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for product in products:
        main_page.add_product_to_cart(product)

    main_page.go_to_cart()
    assert cart_page.get_cart_items() == products
    cart_page.click_checkout()

    checkout_page.fill_form("Иван", "Иванов", "123456")
    total = checkout_page.get_total_price()
    driver.quit()

    assert total == "$58.29", (
        f"Ожидалась сумма '$58.29', но получили '{total}'"
    )
