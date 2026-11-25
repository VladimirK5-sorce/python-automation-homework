# Автотесты на Python (API и Базы данных)

Учебный проект с автоматизированными тестами на **Python**, **pytest**, **Requests** и **SQLAlchemy**.

## Структура проекта

* `lesson_08/` — API-автотесты для сервиса YouGile (методы `POST`, `GET`, `PUT` для проектов) с использованием паттерна PageObject.
* `lesson_09/` — автотесты для проверки CRUD-операций (добавление, изменение, удаление) в базе данных PostgreSQL через SQLAlchemy.

## Установка и запуск

1. Клонируйте репозиторий и установите зависимости:
   ```bash
   pip install pytest requests sqlalchemy psycopg2-binary python-dotenv flake8
   ```

2. Создайте файл `.env` в корне проекта на основе шаблона `.env.example` и укажите ваши данные:
   ```env
   DB_CONNECTION_STRING=postgresql+psycopg://postgres:ваш_пароль@localhost:5432/postgres
   ```

3. Запустите автотесты для базы данных (Задание 9):
   ```bash
   pytest lesson_09
   ```

4. Проверка соответствия стандарту PEP8:
   ```bash
   flake8 lesson_09
   ```
