from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """Функция проверяет наличие одного объекта, при наличии возвращает True"""
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_all_elements_present(self, how, what):
        """Функция проверяет наличие нескольких объектов, при наличии хотя бы одного возвращает True"""
        if len(self.browser.find_elements(how, what)) == 0:
            return False
        else:
            return True

    def is_not_element_present(self, how, what, timeout=4):
        """Функция проверяет отсутствие одного объекта, при наличии возвращает False"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_not_all_elements_present(self, how, what, timeout=4):
        """Функция проверяет отсутствие нескольких объектов, при наличии хотя бы одного возвращает False"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_all_elements_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """Функция проверяет, что элемент пропадает на странице через заданное время, если не пропал, возвращает False"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
