## Генерация и просмотр отчёта Allure (Задание 10)

1. Установите библиотеку для интеграции pytest с Allure:
   ```bash
   pip install allure-pytest
   ```

2. Запустите автотесты из папки `lesson_10` с сохранением результатов для отчёта:
   ```bash
   pytest lesson_10 --alluredir=allure-results
   ```

3. Сформируйте и откройте интерактивный HTML-отчёт в браузере:
   ```bash
   allure serve allure-results
   ```

4. Проверка стиля кода по стандарту PEP8:
   ```bash
   flake8 lesson_10
   ```
