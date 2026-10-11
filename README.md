# UI-тесты Яндекс Самокат

Автотесты интерфейса [Яндекс Самокат](https://qa-scooter.praktikum-services.ru) на Python, pytest и Playwright (Page Object).


## Подготовка (локально)

1. Python 3.11+
2. Виртуальное окружение и зависимости:

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

`playwright install` ставит браузеры (chromium / firefox / webkit), которые использует pytest-playwright.

## Запуск тестов

Окружение задаётся флагом `--env`: `dev` или `stage` (см. `config/environments.py`).

```bash
pytest                 # по умолчанию: env=dev, браузер chromium (pytest-playwright)
pytest --env=dev
pytest --env=stage
```

Если URL stage отличается от dev, задайте его в `config/environments.py`.

### Полезные флаги

| Флаг | Значения | Откуда | По умолчанию |
|------|----------|--------|--------------|
| `--env` | `dev`, `stage` | `conftest.py` | `dev` |
| `--user-type` | `user`, `admin` | `conftest.py` | пользователь окружения из `environments.py` |
| `--browser` | `chromium`, `firefox`, `webkit` | pytest-playwright | `chromium` |
| `--headed` | без значения | pytest-playwright | headless (без флага) |

Примеры:

```bash
pytest --browser=firefox
pytest --headed
pytest -m smoke
pytest -m regression
```

Результаты Allure пишутся в `allure-results` (`--alluredir` в `pytest.ini`).

## Allure

1. Установите [Allure Commandline](https://github.com/allure-framework/allure2/releases); нужна Java, команда `allure` должна быть в `PATH`.
2. Откройте отчёт:

```bash
allure serve allure-results
```

Или статическая сборка:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Docker

Контейнер нужен, чтобы прогонять тесты без локального Python-окружения и установки браузеров. Образ — официальный Playwright Python (`mcr.microsoft.com/playwright/python:v1.62.0-jammy`): Python, зависимости проекта и браузеры Playwright уже внутри.

В `docker-compose.yaml`:

- сервис: `tests`
- контейнер: `samokat-playwright-tests`
- том `./allure-results:/app/allure-results` — сырые результаты Allure на хосте
- том `./playwright-report:/app/playwright-report` — отчёт Playwright (если используется)

Нужны Docker Desktop / Docker Engine и Compose.

Сборка образа и прогон всех тестов:

```bash
docker compose up --build
```

`CMD` в Dockerfile: `pytest -v --alluredir=./allure-results --browser=chromium`. После завершения контейнер останавливается, результаты лежат в `./allure-results`. Отчёт на хосте:

```bash
allure serve allure-results
```

Другое окружение или набор тестов — через `run` (подменяется `CMD` из Dockerfile):

```bash
docker compose run --rm tests pytest --env=stage
docker compose run --rm tests pytest -m smoke
docker compose run --rm tests pytest --browser=firefox
```
