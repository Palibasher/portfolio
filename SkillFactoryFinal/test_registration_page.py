import pytest
from .pages.auth_page import AuthPage
from .pages.base_page import BasePage
from .pages.register_page import RegiserPage
from .pages.sms_email_page import SMSEmailPage
from .pages.locators import Main_Servises_Links as MSL
from random import randint
import time




@pytest.mark.page_integrity
def test_register_page_has_all_valid_elements_key_web(browser):
    """Проверка наличия всех основных элементов формы регистрации
     для страницы Key Web. Ссылка ведет на титульную страницу сайта"""
    link = MSL.KEY_WEB  # ссылка на страницу Ключ Web
    page_title = BasePage(browser, link)  # инициализируем страницу
    page_title.open()  # открываем страницу
    page_title.go_to_login_page_from_key_page()  # переходим на страницу аутентификации по временному коду
    page_temp_code = AuthPage(browser, browser.current_url)  # инициализируем страницу аутентификации
    page_temp_code.go_to_auth_page_from_temp_code_page()  # переходим на основную страницу аутентификации
    page_auth = AuthPage(browser, browser.current_url)  # инициализируем страницу основную страницу аутентификации
    page_auth.go_to_register_page()
    page = RegiserPage(browser, browser.current_url)
    page.should_be_register_page()



@pytest.mark.page_integrity
@pytest.mark.parametrize("link", [MSL.START_WEB,
                                  MSL.SMART_HOME_WEB])
def test_register_page_has_all_valid_elements(browser, link):
    """Проверка наличия всех основных элементов формы регистрации
     для страниц Start Web и SmartHome Web. Ссылка ведет на титульную страницу сайта"""
    page_temp_code = AuthPage(browser, link)
    page_temp_code.open()
    page_temp_code.go_to_auth_page_from_temp_code_page()
    page_auth = AuthPage(browser, browser.current_url)
    page_auth.go_to_register_page()
    page = RegiserPage(browser, browser.current_url)
    page.should_be_register_page()


@pytest.mark.page_integrity
def test_register_page_has_all_valid_elements(browser):
    """Проверка наличия всех основных элементов страницы регистрации
    для страницы ЕЛК WEB"""
    link = MSL.ELK_WEB
    page_auth = AuthPage(browser, link)
    page_auth.open()
    page_auth.go_to_register_page()
    page = RegiserPage(browser, browser.current_url)
    page.should_be_register_page()


@pytest.mark.page_integrity
def test_sms_email_code_page_has_all_valid_elements_elk(browser):
    """Проверка наличия всех основных элементов страницы ввода кода из письма,
    для подтверждения регистрации для страницы ELK_WEB"""
    link = MSL.ELK_WEB
    page_auth = AuthPage(browser, link)
    page_auth.open()
    page_auth.go_to_register_page()
    page = RegiserPage(browser, browser.current_url)
    page.should_be_register_page()
    user = page.generate_new_user()
    page.pick_region_in_region_field()
    page.pick_firstname_field().send_keys(user["firstname"])
    page.pick_lastname_field().send_keys(user["lastname"])
    page.pick_email_phone_field().send_keys(user["email"])
    page.pick_password_field().send_keys(user["password"])
    page.pick_password_conf_field().send_keys(user["password"])
    page.push_confirm_register_button()
    email_code_page = SMSEmailPage(browser, browser.current_url)
    email_code_page.should_be_sms_email_page(user["email"])

@pytest.mark.negative
@pytest.mark.xfail
def test_verificate_registration_with_invalid_verification_code(browser):
    """Проверка возможности подтвердить регистрацию невалидным кодом верификации"""
    link = MSL.ELK_WEB
    page_auth = AuthPage(browser, link)
    page_auth.open()
    page_auth.go_to_register_page()
    page = RegiserPage(browser, browser.current_url)
    page.should_be_register_page()
    user = page.generate_new_user()
    page.pick_region_in_region_field()
    page.pick_firstname_field().send_keys(user["firstname"])
    page.pick_lastname_field().send_keys(user["lastname"])
    page.pick_email_phone_field().send_keys(user["email"])
    page.pick_password_field().send_keys(user["password"])
    page.pick_password_conf_field().send_keys(user["password"])
    page.push_confirm_register_button()
    email_code_page = SMSEmailPage(browser, browser.current_url)
    email_code_page.input_verification_code("111111")

@pytest.mark.negative
@pytest.mark.xfail
@pytest.mark.parametrize("password", ["12a",
                                      "abcdefghi",
                                      "abcdefghiA12abcdefghiA12abcdefghiA12abcdefghiA12abcdefghiA12abcdefghiA12"])
def test_registration_with_unacceptable_password(browser, password):
    """Проверка возможности зарегистрировать нового пользователя с непримлимыми выриантами пароля"""
    link = MSL.ELK_WEB
    page_auth = AuthPage(browser, link)
    page_auth.open()
    page_auth.go_to_register_page()
    page = RegiserPage(browser, browser.current_url)
    page.should_be_register_page()
    user = page.generate_new_user()
    page.pick_region_in_region_field()
    page.pick_firstname_field().send_keys(user["firstname"])
    page.pick_lastname_field().send_keys(user["lastname"])
    page.pick_email_phone_field().send_keys(user["email"])
    page.pick_password_field().send_keys(password)
    page.pick_password_conf_field().send_keys(password)
    page.push_confirm_register_button()
    time.sleep(2)
    page.should_be_same_page()


@pytest.mark.negative
@pytest.mark.xfail
def test_registration_with_empty_name_lastname_fields(browser):
    """Проверка возможности зарегистрировать нового пользователя с пустыми полнями имя, фамилия"""
    link = MSL.ELK_WEB
    page_auth = AuthPage(browser, link)
    page_auth.open()
    page_auth.go_to_register_page()
    page = RegiserPage(browser, browser.current_url)
    page.should_be_register_page()
    user = page.generate_new_user()
    page.pick_region_in_region_field()
    page.pick_email_phone_field().send_keys(user["email"])
    page.pick_password_field().send_keys(user["password"])
    page.pick_password_conf_field().send_keys(user["password"])
    page.push_confirm_register_button()
    time.sleep(2)
    page.should_be_same_page()

@pytest.mark.negative
@pytest.mark.xfail
def test_registration_with_unacceptable_name_lastname_fields(browser):
    """Проверка возможности зарегистрировать нового пользователя
    с полями имя, фамилия заполненными латиницей"""
    link = MSL.ELK_WEB
    page_auth = AuthPage(browser, link)
    page_auth.open()
    page_auth.go_to_register_page()
    page = RegiserPage(browser, browser.current_url)
    page.should_be_register_page()
    user = page.generate_new_user()
    page.pick_region_in_region_field()
    page.pick_firstname_field().send_keys("Jack")
    page.pick_lastname_field().send_keys("Sparrow")
    page.pick_email_phone_field().send_keys(user["email"])
    page.pick_password_field().send_keys(user["password"])
    page.pick_password_conf_field().send_keys(user["password"])
    page.push_confirm_register_button()
    time.sleep(20)
    page.should_be_same_page()