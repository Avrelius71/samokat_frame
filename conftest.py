import pytest

from config.environments import Environment, environments, print_environment_info, common_users
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.order_page import OrderPage


def pytest_addoption(parser):
    """Добавляем опции для выбора окружения и типа пользователя."""
    parser.addoption("--env", default="dev", choices=[e.value for e in Environment],
                     help="Выберите окружение: dev или stage")
    parser.addoption("--user-type", default=None, choices=common_users.keys(),
                     help="Выберите тип пользователя: user или admin")

def pytest_configure(config):
    """Выводит информацию о тестовом окружении перед запуском."""
    env_name = config.getoption("--env")
    user_type = config.getoption("--user-type")
    print_environment_info(env_name, user_type)


@pytest.fixture(scope="session")
def env_config(request):
    """Предоставляет конфигурацию окружения (URL и т.д.)."""
    env_name = request.config.getoption("--env")
    return environments[Environment(env_name)]


@pytest.fixture(scope="session")
def base_url(env_config):
    return env_config.url


@pytest.fixture(autouse=True)
def _apply_base_url(base_url):
    """Прокидывает URL выбранного окружения во все Page Object'ы."""
    BasePage.BASE_URL = base_url


@pytest.fixture
def order(page):
    return OrderPage(page)


@pytest.fixture
def home(page):
    return HomePage(page)
