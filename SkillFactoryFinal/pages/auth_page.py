from .base_page import BasePage
from .locators import AuthPageLocators

class AuthPage(BasePage):

    def go_to_auth_page_from_temp_code_page(self):
        button = self.browser.find_element(*AuthPageLocators.BUTTON_STANDART_AUT)
        button.click()

    def go_to_register_page(self):
        button = self.browser.find_element(*AuthPageLocators.BUTTON_REGISTER)
        button.click()

    #проверки наличия всех основых элементов на странице авторизации по временному коду
    def should_be_auth_page_login_by_temp_code(self):
        """Проверка, что попали на страницу авторизации, авторизация по временному коду,
         все ожидаемые элементы присутсвуют"""
        self.should_be_valid_logo()                  #лого соответствует странице
        self.should_be_temp_code_auth_text()         #текст соответствует странице
        self.should_be_temp_code_email_phone_field() #поле для ввода почты или телефона присутствует
        self.should_be_temp_code_get_code_button()   #кнопка для получения кода присутствует
        self.should_be_standart_auth_button()        #кнопка перехода к стандартной авторизации присутствует

    def should_be_valid_logo(self):
        """Проверка корректности логотипа, в зависимости от типа страницы"""
        if "lk_smarthome" in self.browser.current_url:
            assert self.is_element_present(*AuthPageLocators.LOGO_SMART_HOME), "Invalid logo for Smart Home"
        elif "lk_dmh" in self.browser.current_url:
            assert self.is_element_present(*AuthPageLocators.LOGO_RT_KEY), "Invalid logo for RT Key"
        else:
            assert self.is_element_present(*AuthPageLocators.LOGO_MAINLOGO_RT), "Invalid main RT logo"

    def should_be_temp_code_auth_text(self):
        assert self.find_element_wait_for_it(*AuthPageLocators.TEXT_MAIN_TITLE_TEMP).text == "Авторизация по коду", "Invalid is text"

    def should_be_temp_code_email_phone_field(self):
        assert self.is_element_present(*AuthPageLocators.FIELD_TEMP_CODE_EMAIL_PHONE), "EMAIL_PHONE field is missing"

    def should_be_temp_code_get_code_button(self):
        assert self.is_element_present(*AuthPageLocators.BUTTON_GET_TEMP_CODE), "Get code button is missing"

    def should_be_standart_auth_button(self):
        assert self.is_element_present(*AuthPageLocators.BUTTON_STANDART_AUT), "Standart auth button is missing"

    #проверки наличия всех основых элементов на странице авторизации
    def should_be_auth_page(self):
        """Проверка, что попали на страницу авторизации, авторизация по временному коду,
         все ожидаемые элементы присутсвуют"""
        self.should_be_auth_text()
        self.should_be_switch_tabs()
        self.should_be_log_pass_fields()
        self.should_be_log_in_button()
        self.should_be_back_to_temp_code_button()
        self.should_be_register_button()


    def should_be_auth_text(self):
        assert self.find_element_wait_for_it(*AuthPageLocators.TEXT_MAIN_TITLE_TEMP).text == "Авторизация"

    def should_be_switch_tabs(self):
        assert self.is_element_present(*AuthPageLocators.TAB_LOGIN), "Login tab is missing"
        assert self.is_element_present(*AuthPageLocators.TAB_PHONE), "Phone tab is missing"
        assert self.is_element_present(*AuthPageLocators.TAB_MAIL), "Mail tab is missing"
        if "lk_decosystems" in self.browser.current_url or "lk_b2c" in self.browser.current_url:
            assert self.is_element_present(*AuthPageLocators.TAB_LS), "LS tab is missing"

    def should_be_log_pass_fields(self):
        assert self.is_element_present(*AuthPageLocators.FIELD_MAIN_LOGIN), "Login field is missing"
        assert self.is_element_present(*AuthPageLocators.FIELD_PASSWORD), "Password field is missing"

    def should_be_log_in_button(self):
        assert self.is_element_present(*AuthPageLocators.BUTTON_SUBMIT_LOGIN_USER), "Login button submit is missing"

    def should_be_back_to_temp_code_button(self):
        if "lk_b2c" not in self.browser.current_url:
            assert self.is_element_present(*AuthPageLocators.BUTTON_BACK_TO_TEMP_CODE_AUTH), "Back to temp code button is missing"

    def should_be_register_button(self):
        if "lk_onlime" not in self.browser.current_url:
            assert self.is_element_present(*AuthPageLocators.BUTTON_REGISTER), "Register button is missing"

    def send_data_to_auth_page_field(self, flag_email, flag_pass):
        flag_email = flag_email
        flag_pass = flag_pass
        self.find_element_wait_for_it(*AuthPageLocators.FIELD_MAIN_LOGIN).send_keys(AuthPageLocators.EMAIL_VAR[flag_email])
        self.find_element_wait_for_it(*AuthPageLocators.FIELD_PASSWORD).send_keys(AuthPageLocators.PASSWORD_VAR[flag_pass])

    def click_logon_button(self):
        self.find_element_wait_for_it(*AuthPageLocators.BUTTON_SUBMIT_LOGIN_USER).click()

    def should_be_error_msg(self):
        assert self.find_element_wait_for_it(*AuthPageLocators.TEXT_ERROR_MESSAGE)


