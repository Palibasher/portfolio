import pytest
from random import randint
import time
import selenium.common.exceptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        name = "".join([chr(randint(97, 122)) for i in range(randint(8, 15))])  # генерируем email
        host = "".join([chr(randint(97, 122)) for i in range(randint(8, 15))])
        email = f"{name}@{host}.com"
        password = "".join([chr(randint(97, 122)) for i in range(randint(8, 15))])  # генерируем password
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login"
        login_page = LoginPage(browser, link)  # инициализируем страницу
        login_page.open()  # открываем страницу
        login_page.register_new_user(email, password)  # регистрируем пользователя

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)  # инициализируем страницу
        page.open()  # открываем страницу
        page.should_not_be_success_message()  # проверяем что сообщения не появились

    @pytest.mark.need_review
    def test_user_can_add_item_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_item_to_basket()  # выполняем метод страницы — добавляем товар в корзину
        page.solve_quiz_and_get_code()  # решаем задачку для роботов
        page.should_be_correct_name_in_alert_message_after_item_add()  # проверяем корректность названия в появившемся сообщение
        page.should_be_correct_price_in_alert_message_after_item_add()  # проверяем корректность цены в появившемся сообщение


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_item_to_basket()  # добавляем товар в корзину
    page.should_not_be_success_message()  # проверяем что сообщения не появились


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()  # проверяем что сообщения не появились


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_item_to_basket()  # добавляем товар в корзину
    page.should_success_message_is_disappear()  # проверяем что сообщения пропали


@pytest.mark.need_review
def test_guest_can_add_item_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_item_to_basket()  # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()  # решаем задачку для роботов
    page.should_be_correct_name_in_alert_message_after_item_add()  # проверяем корректность названия в появившемся сообщение
    page.should_be_correct_price_in_alert_message_after_item_add()  # проверяем корректность цены в появившемся сообщение


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_item_to_basket_promo(browser, link):
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_item_to_basket()  # выполняем метод страницы — добавляем товар в корзину
    page.solve_quiz_and_get_code()  # решаем задачку для роботов
    page.should_be_correct_name_in_alert_message_after_item_add()  # проверяем корректность названия в появившемся сообщение
    page.should_be_correct_price_in_alert_message_after_item_add()  # проверяем корректность цены в появившемся сообщение


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_item_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_basket_empty()
