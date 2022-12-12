from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert self.browser.current_url[-6:] == "login/", "Incorrect LoginPage url"

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"


    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_FIELD)
        email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS_FIELD)
        pass_field.send_keys(password)
        pass_field_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASS_CONFIRM_FIELD)
        pass_field_confirm.send_keys(password)
        confirm_button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM_BUTTON)
        confirm_button.click()
        self.should_be_authorized_user()
