from dataclasses import dataclass
from enum import Enum
from config.settings import settings


class Environment(str, Enum):
    DEV = "dev"
    STAGE = "stage"

    def __str__(self):
        return {"dev": "Dev", "stage": "Stage"}[self.value]


@dataclass
class EnvironmentConfig:
    url: str
    default_user_type: str

    def __str__(self):
        return f"- URL: {self.url}"


environments = {
    Environment.DEV: EnvironmentConfig(
        url="https://qa-scooter.praktikum-services.ru",
        default_user_type="admin"
    ),
    Environment.STAGE: EnvironmentConfig(
        url="https://qa-scooter.praktikum-services.ru",  # замени на stage-URL когда появится
        default_user_type="user"
    )
}


def get_user_credentials(user_type: str) -> tuple[str, str]:
    """Безопасно достает email и пароль из .env по типу пользователя."""
    if user_type == "admin":
        return settings.admin_email, settings.admin_password
    elif user_type == "user":
        return settings.user_email, settings.user_password
    raise ValueError(f"Неизвестный тип пользователя '{user_type}'. Используй 'user' или 'admin'.")


def print_environment_info(env_name: str, user_type: str = None):
    """Выводит краткую сводку по тестовому окружению."""
    env = Environment(env_name)
    config = environments[env]

    # Если тип не передан, берем дефолтный для этого окружения
    final_user_type = user_type or config.default_user_type

    # Достаем реальные креды из .env через нашу безопасную функцию
    email, _ = get_user_credentials(final_user_type)

    print()
    print(f"Окружение:    {str(env)}")
    print(f"URL:          {config.url}")
    print(f"Пользователь: {email}")
    print()