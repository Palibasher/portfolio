import time

from .base_page import BasePage
from .locators import SMS_Email_Page_Locators

class SMSEmailPage(BasePage):

    def should_be_sms_email_page(self, email):
        self.should_be_input_fields()
        self.should_be_valid_title()
        self.should_be_valid_email(email)
        self.should_be_timer()

    def should_be_input_fields(self):
        assert self.is_element_present(*SMS_Email_Page_Locators.FIELD_CODE_1), "Field 1 for code is missing"
        assert self.is_element_present(*SMS_Email_Page_Locators.FIELD_CODE_2), "Field 2 for code is missing"
        assert self.is_element_present(*SMS_Email_Page_Locators.FIELD_CODE_3), "Field 3 for code is missing"
        assert self.is_element_present(*SMS_Email_Page_Locators.FIELD_CODE_4), "Field 4 for code is missing"
        assert self.is_element_present(*SMS_Email_Page_Locators.FIELD_CODE_5), "Field 5 for code is missing"
        assert self.is_element_present(*SMS_Email_Page_Locators.FIELD_CODE_6), "Field 6 for code is missing"

    def should_be_valid_title(self):
        assert self.find_element_wait_for_it(*SMS_Email_Page_Locators.TEXT_TITLE).text == "Подтверждение email", "Invalid title"

    def should_be_valid_email(self, email):
        assert email in self.find_element_wait_for_it(*SMS_Email_Page_Locators.TEXT_EMAIL).text, "Wrong email name"

    def should_be_timer(self):
        assert self.is_element_present(*SMS_Email_Page_Locators.TEXT_TIMER), "Timer is missing"

    def input_verification_code(self, code):
        code = code
        code_page_url = self.browser.current_url
        self.find_element_wait_for_it(*SMS_Email_Page_Locators.FIELD_CODE_1).send_keys(code[0])
        self.find_element_wait_for_it(*SMS_Email_Page_Locators.FIELD_CODE_2).send_keys(code[1])
        self.find_element_wait_for_it(*SMS_Email_Page_Locators.FIELD_CODE_3).send_keys(code[2])
        self.find_element_wait_for_it(*SMS_Email_Page_Locators.FIELD_CODE_4).send_keys(code[3])
        self.find_element_wait_for_it(*SMS_Email_Page_Locators.FIELD_CODE_5).send_keys(code[4])
        self.find_element_wait_for_it(*SMS_Email_Page_Locators.FIELD_CODE_6).send_keys(code[5])
        time.sleep(3)
        assert self.browser.current_url != code_page_url

