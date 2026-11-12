from pages.base_page import BasePage
from playwright.sync_api import Page, expect, Locator


class HomePage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.header_button_order = self.page.get_by_role('button', name='Заказать').first
        self.content_button_order = self.page.get_by_role('button', name='Заказать', exact=True).last
        self.link_yandex = self.page.get_by_role('link', name='Yandex')
        self.link_samokat = self.page.get_by_role('link', name='Scooter')

    def search_droplist(self, index: int) -> Locator:
        return self.page.locator(f'#accordion__heading-{index}')

    def droplist_of_answers(self, index: int) -> Locator:
        return self.page.locator(f'#accordion__panel-{index}')

    def header_button_order_click(self) -> None:
        self.header_button_order.click()

    def content_button_order_click(self) -> None:
        self.content_button_order.click()

    def click_search_droplist(self, index: int) -> None:
        self.search_droplist(index).click()

    def check_search_droplist(self, index: int, text: str) -> None:
        answer = self.droplist_of_answers(index)
        expect(answer).to_be_visible()
        expect(answer).to_have_text(text)

    def click_and_check_yandex_link(self) -> Page:
        with self.page.expect_popup() as page_info:
            self.link_yandex.click()
        page_2 = page_info.value
        page_2.wait_for_load_state()
        assert 'dzen.ru' in page_2.url, 'Открылась другая страница'
        return page_2

    def click_samokat_link(self) -> None:
        self.link_samokat.click()
