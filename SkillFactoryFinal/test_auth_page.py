import selenium.common.exceptions
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .pages.auth_page import AuthPage
from .pages.base_page import BasePage
from .pages.register_page import RegiserPage
from .pages.locators import Main_Servises_Links as MSL



@pytest.mark.page_integrity
@pytest.mark.parametrize("link", [MSL.ONLAIM_WEB,
                                  MSL.START_WEB,
                                  MSL.SMART_HOME_WEB])
def test_temporarily_code_page_has_all_valid_elements_dirrect_pages(browser, link):
    """Проверка наличия всех основных элементов на странице авторизации по временному коду"""
    link = link
    page = AuthPage(browser, link)
    page.open()
    page.should_be_auth_page_login_by_temp_code()


@pytest.mark.page_integrity
def test_temporarily_code_page_has_all_valid_elements_indirrect_page(browser):
    """Проверка наличия всех основных элементов на странице авторизации по временному коду
    Так как ссылка не ведет на страницу авторизации, 
    сначала проверяем наличие кнопки для перехода и переходим по ней"""
    link = MSL.KEY_WEB
    rt_key_page = BasePage(browser, link)
    rt_key_page.open()
    rt_key_page.should_be_login_link_from_key_page()
    rt_key_page.go_to_login_page_from_key_page()
    page = AuthPage(browser, browser.current_url)
    page.open()
    page.should_be_auth_page_login_by_temp_code()



@pytest.mark.page_integrity
@pytest.mark.parametrize("link", [MSL.ONLAIM_WEB,
                                  MSL.START_WEB,
                                  MSL.SMART_HOME_WEB])
def test_auth_page_has_all_valid_elements(browser, link):
    """Проверка наличия всех основных элементов основной формы авторизации,
    Для сервисов ссылка на которые ведет на страницу с временным кодом"""
    page_temp_code = AuthPage(browser, link)
    page_temp_code.open()
    page_temp_code.go_to_auth_page_from_temp_code_page()
    page_aut = AuthPage(browser, browser.current_url)
    page_aut.should_be_auth_page()


@pytest.mark.page_integrity
def test_auth_page_has_all_valid_elements_elk_web(browser):
    """Проверка наличия всех основных элементов основной формы авторизации
     для страницы ЕЛК Web. Ссылка ведет на основную форму авторизации"""
    link = MSL.ELK_WEB
    page = AuthPage(browser, link)
    page.open()
    page.should_be_auth_page()


@pytest.mark.page_integrity
def test_auth_page_has_all_valid_elements_key_web(browser):
    """Проверка наличия всех основных элементов основной формы авторизации
     для страницы Key Web. Ссылка ведет на титульную страницу сайта"""
    link = MSL.KEY_WEB                                        #ссылка на страницу Ключ Web
    page_title = BasePage(browser, link)                      #инициализируем страницу
    page_title.open()                                         #открываем страницу
    page_title.go_to_login_page_from_key_page()               #переходим на страницу аутентификации по временному коду
    page_temp_code = AuthPage(browser, browser.current_url)   #инициализируем страницу аутентификации
    page_temp_code.open()                                     #открываем страницу
    page_temp_code.go_to_auth_page_from_temp_code_page()      #переходим на основную страницу аутентификации
    page = AuthPage(browser, browser.current_url)             #инициализируем страницу основную страницу аутентификации
    page.should_be_auth_page()                                #проверяем основную страницу аутентификации


@pytest.mark.need_rewiew
def test_user_can_autorize_vith_valid_data_elk(browser):
    """Проверка авторизации с валидными данными"""
    link = MSL.ELK_WEB
    page = AuthPage(browser, link)
    page.open()
    page.send_data_to_auth_page_field("EMAIL", "PASSWORD")
    page.click_logon_button()
    time.sleep(10)
    lk_page = BasePage(browser, browser.current_url)
    lk_page.is_it_lk_page()


@pytest.mark.negative
def test_user_can_not_autorize_vith_incomplete_data_elk(browser):
    """Проверка возможности авторизации с частичным email"""
    link = MSL.ELK_WEB
    page = AuthPage(browser, link)
    page.open()
    page.send_data_to_auth_page_field("EMAIL_INCOMPLETE", "PASSWORD")
    page.click_logon_button()
    page.should_be_error_msg()

@pytest.mark.negative
def test_user_can_not_autorize_vith_wrong_pass_data_elk(browser):
    """Проверка возможности авторизации с невалидным паролем"""
    link = MSL.ELK_WEB
    page = AuthPage(browser, link)
    page.open()
    page.send_data_to_auth_page_field("EMAIL", "WRONG_PASSWORD")
    page.click_logon_button()
    page.should_be_error_msg()
