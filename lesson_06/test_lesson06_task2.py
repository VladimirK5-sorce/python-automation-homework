from selenium import webdriver


def test_cookie_auth():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        driver.get("https://gitflic.ru")

        cookie_1 = {
            "name": "gitflic_session",
            "value": "Mze4MjRjZmUtZWQ4YS00YTA3LTllMTUtYjA1ZGYzNjQxNmM2"
        }
        driver.add_cookie(cookie_1)
        driver.refresh()

        driver.get("https://gitflic.ru/user/volod")
        user1_url = driver.current_url

        driver.delete_all_cookies()

        cookie_2 = {
            "name": "gitflic_session",
            "value": "NDBiODQxMDMtZWU5Yi00MmI2LWE1ZDKtY2UxMDY5ZWE0Y2Yy"
        }
        driver.add_cookie(cookie_2)
        driver.refresh()

        driver.get("https://gitflic.ru/user/statham")
        user2_url = driver.current_url

        assert user1_url != user2_url, (
            f"Ошибка: оба токена ведут на один URL {user1_url}"
        )
    finally:
        driver.quit()
