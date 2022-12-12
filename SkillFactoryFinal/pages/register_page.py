from .base_page import BasePage
from .locators import Registration_Page_Locators
import time
from random import randint


class RegiserPage(BasePage):

    def should_be_register_page(self):
        self.should_be_firstmane_field()
        self.should_be_lastmane_field()
        self.should_be_region_field()
        self.should_be_email_phone_field()
        self.should_be_pass_field()
        self.should_be_pass_conformation_field()


    def should_be_region_field(self):
        assert self.is_element_present(*Registration_Page_Locators.FIELD_REGION), "Region field is missing"

    def should_be_email_phone_field(self):
        assert self.is_element_present(*Registration_Page_Locators.FIELD_EMAIL_PHONE), "Email/Phone field is missing"

    def should_be_firstmane_field(self):
        assert self.is_element_present(*Registration_Page_Locators.FIELD_FIRSTNAME), "First name field is missing"

    def should_be_lastmane_field(self):
        assert self.is_element_present(*Registration_Page_Locators.FIELD_LASTNAME), "Lastname name field is missing"

    def should_be_pass_field(self):
        assert self.is_element_present(*Registration_Page_Locators.FIELD_PASS), "Password field is missing"

    def should_be_confirm_button(self):
        assert self.is_element_present(*Registration_Page_Locators.BUTTON_CONFIRM_REGISTER), "Confirm regist button is missing"

    def should_be_pass_conformation_field(self):
        assert self.is_element_present(*Registration_Page_Locators.FIELD_PASS_CONF), "Password conformation field is missing"

    def pick_region_in_region_field(self):
        button = self.browser.find_element(*Registration_Page_Locators.REGION_DROP_DOWN_ARROW)
        button.click()
        button = self.browser.find_element(*Registration_Page_Locators.REGION_DROP_DOWN_ELEMENT)
        button.click()

    def generate_new_user(self):
        email_name = "".join([chr(randint(97, 122)) for i in range(randint(8, 15))])  # генерируем email
        email = f"{email_name}@yandex.ru"
        password = "".join([chr(randint(97, 122)) for i in range(randint(8, 15))]) + "A1"  # генерируем password
        firstname = "Иван"
        lastname = "Тестов"
        return {"firstname" : firstname, "lastname" : lastname, "email" : email, "password" : password}

    def pick_firstname_field(self):
        return self.find_element_wait_for_it(*Registration_Page_Locators.FIELD_FIRSTNAME)

    def pick_lastname_field(self):
        return self.find_element_wait_for_it(*Registration_Page_Locators.FIELD_LASTNAME)

    def pick_email_phone_field(self):
        return self.find_element_wait_for_it(*Registration_Page_Locators.FIELD_EMAIL_PHONE)

    def pick_password_field(self):
        return self.find_element_wait_for_it(*Registration_Page_Locators.FIELD_PASS)

    def pick_password_conf_field(self):
        return self.find_element_wait_for_it(*Registration_Page_Locators.FIELD_PASS_CONF)

    def push_confirm_register_button(self):
        self.find_element_wait_for_it(*Registration_Page_Locators.BUTTON_CONFIRM_REGISTER).click()



