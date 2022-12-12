from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .locators import Key_RT_Locators
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import ElementNotInteractableException
from .locators import AuthPageLocators




class BasePage():
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # БАЗОВЫЕ ФУНКЦИИ ПРОВЕРКИ И ОТКРЫТИЯ СТРАНИЦЫ
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

    def is_not_element_present(self, how, what, timeout=5):
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

    def find_element_wait_for_it(self, how, what, timeout=20):
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))

    #Проверка присутвия ссылки на странице https://key.rt.ru/
    def should_be_login_link_from_key_page(self):
        assert self.is_element_present(*Key_RT_Locators.BUTTON_LOGIN), "Login link is not presented"

    # Переход по ссылке на странице https://key.rt.ru/
    def go_to_login_page_from_key_page(self):
        try:
            link = self.find_element_wait_for_it(*Key_RT_Locators.BUTTON_LOGIN)
            link.click()
        except (ElementNotInteractableException):
            self.browser.get("https://key.rt.ru/main/pwa")

    def switch_back_home(self):
        self.browser.switch_to.window(self.browser.window_handles[0])

    def switch_to_external(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def is_it_lk_page(self):
        assert "lk.rt.ru" in self.browser.current_url

    def should_be_same_page(self):
        code_page_url = self.browser.current_url
        time.sleep(3)
        assert self.browser.current_url != code_page_url