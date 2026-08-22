import allure
import pytest


@pytest.mark.regression
@allure.feature('FAQ and navigations')
class TestHome:

    @pytest.mark.parametrize('index, search', [
        (0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (1, 'Пока что у нас так: один заказ — один самокат. '
            'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
            'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
            'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (5, 'Самокат приезжает к вам с полной зарядкой. '
            'Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. '
            'Зарядка не понадобится.'),
        (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ])
    @pytest.mark.smoke
    @allure.title("Блок FAQ")
    def test_search(self, home, index, search):
        with allure.step('Открываем главную страницу'):
            home.open()

        with allure.step('Проверка открывания дроплиста по вопросам'):
            home.click_search_droplist(index)

        with allure.step('Проверка вопросов'):
            home.check_search_droplist(index, search)

    @allure.title("Навигация на кнопку 'Яндекс'")
    def test_navigation_link_yandex(self, home):
        with allure.step('Открываем главную страницу'):
            home.open()

        with allure.step('Проверяем навигацию'):
            home.click_and_check_yandex_link()

    @allure.title("Навигация на кнопку 'Самокат'")
    def test_navigation_link_samokat(self, home):
        with allure.step('Открываем страницу для заказа самоката'):
            home.open('/order')

        with allure.step('Проверяем навигацию'):
            home.click_samokat_link()
            home.check_url('/')
