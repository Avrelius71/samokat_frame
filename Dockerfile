FROM mcr.microsoft.com/playwright/python:v1.62.0-jammy

WORKDIR /app

# Дефолтный браузер. Переопределяется через env_file / -e / command в compose.
ENV BROWSER=chromium

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# .env сюда НЕ попадает благодаря .dockerignore. Секреты живут только в runtime.
COPY . .

# Shell-форма CMD — чтобы подставить переменную BROWSER.
# В exec-форме (["pytest", ...]) переменные окружения не раскрываются, запомни это.
CMD pytest -v --alluredir=./allure-results --browser=${BROWSER}