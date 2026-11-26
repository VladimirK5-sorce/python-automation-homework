import allure
import pytest
from selenium import webdriver
from lesson_10.CartPage import CartPage
from lesson_10.CheckoutPage import CheckoutPage
from lesson_10.LoginPage import LoginPage
from lesson_10.MainPage import MainPage


@pytest.fixture
def firefox_driver():
    """Создаёт и закрывает драйвер Firefox для теста интернет-магазина."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Интернет-магазин")
@allure.title("Проверка оформления заказа и расчёта итоговой суммы")
@allure.description(
    "Авторизуется в магазине, добавляет три товара в корзину, проверяет "
    "состав корзины, заполняет данные доставки и сверяет итоговую сумму."
)
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_purchase(firefox_driver) -> None:
    login_page = LoginPage(firefox_driver)
    main_page = MainPage(firefox_driver)
    cart_page = CartPage(firefox_driver)
    checkout_page = CheckoutPage(firefox_driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]
    with allure.step("Добавить выбранные товары в корзину"):
        for product in products:
            main_page.add_product_to_cart(product)

    main_page.go_to_cart()

    with allure.step("Проверить, что в корзине отображаются все 3 товара"):
        assert cart_page.get_cart_items() == products

    cart_page.click_checkout()
    checkout_page.fill_form("Иван", "Иванов", "123456")
    total = checkout_page.get_total_price()

    with allure.step("Проверить, что итоговая сумма заказа равна '$58.29'"):
        assert total == "$58.29", (
            f"Ожидалась сумма '$58.29', но получили '{total}'"
        )
