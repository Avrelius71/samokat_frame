from playwright.sync_api import Page, expect


class BasePage:
    BASE_URL = ""

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "/") -> None:
        """Открывает страницу относительно BASE_URL окружения."""
        url = f"{self.BASE_URL.rstrip('/')}{path}"
        self.page.goto(url)

    def check_url(self, path: str) -> None:
        """Проверяет, что текущий URL соответствует path относительно BASE_URL."""
        expected = f"{self.BASE_URL.rstrip('/')}{path}"
        expect(self.page).to_have_url(expected)
