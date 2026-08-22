import allure
import pytest


users = [
    ('Иван', 'Петров', 'Москва', 'Сокольники', '79001234567', '05.08.2026', 'сутки', 'black', 'test1'),
    ('Мария', 'Смирнова', 'Москва', 'Лубянка', '79109876543', '06.08.2026', 'семеро суток', 'grey', 'test2'),
]

ORDER_BUTTONS = [
    ('header', "Заказ самоката через кнопку 'Заказать' в шапке страницы(валидные данные)"),
    ('content', "Заказ самоката через кнопку 'Заказать' в контентной части страницы(валидные данные)"),
]


@pytest.mark.regression
@allure.feature('Order scooter')
class TestOrder:

    @pytest.mark.smoke
    @pytest.mark.parametrize('button, title', ORDER_BUTTONS)
    @pytest.mark.parametrize(
        'firstname, lastname, city, metro, phone, delivery_date, deadlines, color, comment',
        users,
    )
    def test_order_samokat(
            self, order, home, button, title,
            firstname, lastname, city, metro, phone,
            delivery_date, deadlines, color, comment,
    ):
        allure.dynamic.title(title)

        with allure.step('Открываем страницу для заказа самоката'):
            home.open()
            if button == 'header':
                home.header_button_order_click()
            else:
                home.content_button_order_click()

        with allure.step('Проверка формы для заказа самоката'):
            order.check_order_log_and_button()
            order.check_first_input_visible()

        with allure.step('Заполняем 1 блок с информацией'):
            order.fill_name(firstname)
            order.fill_last_name(lastname)
            order.fill_address(city)
            order.fill_metro(metro)
            order.fill_number(phone)

        with allure.step('Переходим на следующий блок и проверяем его'):
            order.next_button.click()
            order.check_logo_rental_and_order_button()

        with allure.step('Заполняем 2 блок с информацией'):
            order.fill_delivery_date(delivery_date)
            order.select_deadlines_choice(deadlines)
            order.radio_button_color_click(color)
            order.fill_input_comment(comment)

        with allure.step('Жмем кнопку для заказа самоката'):
            order.click_order_button()

        with allure.step('Подтверждаем заказ'):
            order.click_button_confirm_form_confirmation()

        with allure.step('Проверяем бы ли сделан заказ'):
            order.check_view_successful_order()
