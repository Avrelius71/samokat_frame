from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class OrderPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.input_name = self.page.locator("//input[@placeholder='* Имя']")
        self.input_lastname = self.page.locator("//input[@placeholder='* Фамилия']")
        self.input_address = self.page.locator("//input[@placeholder='* Адрес: куда привезти заказ']")
        self.input_metro = self.page.locator("//input[@placeholder='* Станция метро']")
        self.input_number = self.page.locator("//input[@placeholder='* Телефон: на него позвонит курьер']")
        self.next_button = self.page.get_by_role('button', name='Далее')
        self.logo_order_page = self.page.locator("//div[text()='Для кого самокат']")
        self.logo_rental_order_page = self.page.locator("//div[text()='Про аренду']")
        self.input_delivery_date = self.page.locator("//input[@placeholder='* Когда привезти самокат']")
        self.select_deadlines = self.page.locator("//div[@class='Dropdown-root']")
        self.black_color_radiobutton = self.page.locator("//input[@id='black']")
        self.grey_color_radiobutton = self.page.locator("//input[@id='grey']")
        self.input_comment = self.page.locator("//input[@placeholder='Комментарий для курьера']")
        self.order_button = self.page.get_by_role('button', name='Заказать').last
        self.back_button = self.page.get_by_role('button', name='Назад')
        self.confirm_button_confirmation_form = self.page.get_by_role('button', name='Да', exact=True)
        self.view_successful_order = self.page.locator("//*[@class='Order_ModalHeader__3FDaJ']")

    def check_order_log_and_button(self) -> None:
        expect(self.logo_order_page).to_be_visible()
        expect(self.logo_order_page).to_have_text('Для кого самокат')
        expect(self.next_button).to_be_visible()

    def check_first_input_visible(self) -> None:
        expect(self.input_name).to_be_visible()
        expect(self.input_lastname).to_be_visible()
        expect(self.input_address).to_be_visible()
        expect(self.input_metro).to_be_visible()
        expect(self.input_number).to_be_visible()

    def fill_name(self, name: str) -> None:
        self.input_name.fill(name)

    def fill_last_name(self, lastname: str) -> None:
        self.input_lastname.fill(lastname)

    def fill_address(self, address: str) -> None:
        self.input_address.fill(address)

    def fill_metro(self, metro: str) -> None:
        self.input_metro.fill(metro)
        self.input_metro.press('ArrowDown')
        self.input_metro.press('Enter')

    def fill_number(self, number: str) -> None:
        self.input_number.fill(number)

    def next_button_click(self) -> None:
        self.next_button.click()

    def fill_delivery_date(self, delivery_date: str) -> None:
        self.input_delivery_date.click()
        self.input_delivery_date.fill(delivery_date)
        self.logo_rental_order_page.click()

    def select_deadlines_choice(self, period: str) -> None:
        self.select_deadlines.click()
        option = self.page.get_by_role('option', name=period, exact=True)
        expect(option).to_be_visible()
        option.click()

    def radio_button_color_click(self, color: str) -> None:
        if color == 'black':
            self.black_color_radiobutton.click()
        elif color == 'grey':
            self.grey_color_radiobutton.click()

    def fill_input_comment(self, comment: str) -> None:
        self.input_comment.fill(comment)

    def click_order_button(self) -> None:
        self.order_button.click()

    def check_logo_rental_and_order_button(self) -> None:
        expect(self.logo_rental_order_page).to_be_visible()
        expect(self.logo_rental_order_page).to_have_text('Про аренду')
        expect(self.order_button).to_be_visible()
        expect(self.order_button).to_be_enabled()
        expect(self.back_button).to_be_visible()
        expect(self.back_button).to_be_enabled()

    def click_button_confirm_form_confirmation(self) -> None:
        self.confirm_button_confirmation_form.click()

    def check_view_successful_order(self) -> None:
        expect(self.view_successful_order).to_contain_text('Заказ оформлен')
