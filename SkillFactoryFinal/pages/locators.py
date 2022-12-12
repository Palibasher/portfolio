from selenium.webdriver.common.by import By

class Main_Servises_Links():
    ELK_WEB = "https://lk.rt.ru/"
    ONLAIM_WEB = "https://my.rt.ru/"
    START_WEB = "https://start.rt.ru/"
    SMART_HOME_WEB = "https://lk.smarthome.rt.ru/"
    KEY_WEB = "https://key.rt.ru/"


class AuthPageLocators():
    #логотипы продуктов
    LOGO_MAINLOGO_RT = (By.CSS_SELECTOR, ".main-header__logo-container")
    LOGO_SMART_HOME = (By.CSS_SELECTOR, ".smarthome-header__logo")
    LOGO_RT_KEY = (By.CSS_SELECTOR, ".dmh-header__logo")
    #элементы основной страницы авторизации
    FIELD_MAIN_LOGIN = (By.ID, "username")
    FIELD_PASSWORD = (By.ID, "password")
    BUTTON_REGISTER = (By.ID, "kc-register")
    BUTTON_SUBMIT_LOGIN_USER = (By.ID, "kc-login")
    TAB_PHONE = (By.ID, "t-btn-tab-phone")
    TAB_MAIL = (By.ID, "t-btn-tab-mail")
    TAB_LOGIN = (By.ID, "t-btn-tab-login")
    TAB_LS = (By.ID, "t-btn-tab-ls")
    BUTTON_BACK_TO_TEMP_CODE_AUTH = (By.ID, "back_to_otp_btn")
    TEXT_ERROR_MESSAGE = (By.ID, "form-error-message")
    #Элементы страницы входа по временному коду
    BUTTON_STANDART_AUT = (By.NAME, "standard_auth_btn")
    FIELD_TEMP_CODE_EMAIL_PHONE = (By.ID, "address")
    BUTTON_GET_TEMP_CODE = (By.ID, "otp_get_code")
    TEXT_MAIN_TITLE_TEMP = (By.CSS_SELECTOR, "h1.card-container__title")
    #элементы страницы перехода
    MAIN_HEADER_MENU_LINKS = (By.CSS_SELECTOR, ".main-header-menu__links")
    MAIN_HEADER_MENU_LINKS2 = (By.CSS_SELECTOR, ".application-header_sector-help")
    MAIN_HEADER_MENU_LINKS3 = (By.CSS_SELECTOR, ".extra-cabinet-link")
    #Test_data
    EMAIL = "aqldvzavofzakowagg@tmmbt.com"

    EMAIL_VAR = {"EMAIL" : "aqldvzavofzakowagg@tmmbt.com",
                 "EMAIL_INCOMPLETE" : "aqldvzavofzakowagg",
                 }
    PASSWORD_VAR = {"PASSWORD" : "12abc!11A",
                    "WRONG_PASSWORD" : "WrongPass!1"
                    }


class Key_RT_Locators():
    BUTTON_LOGIN = (By.CSS_SELECTOR, 'a[href="/main/pwa"].go_kab')

class Registration_Page_Locators():
    FIELD_FIRSTNAME = (By.NAME, "firstName")
    FIELD_LASTNAME = (By.NAME, "lastName")
    FIELD_REGION = (By.CSS_SELECTOR, ".rt-input-container.rt-select__input .rt-input input")
    FIELD_EMAIL_PHONE = (By.CSS_SELECTOR, ".rt-input-container.email-or-phone .rt-input input")
    FIELD_PASS = (By.CSS_SELECTOR, ".new-password-container__password .rt-input input")
    FIELD_PASS_CONF = (By.CSS_SELECTOR, ".new-password-container__confirmed-password .rt-input input")
    REGION_DROP_DOWN_ARROW = (By.CSS_SELECTOR, "svg.rt-select__arrow")
    REGION_DROP_DOWN_ELEMENT = (By.CSS_SELECTOR, ".rt-scroll-container.rt-scrollbar .rt-select__list-item:nth-of-type(5)")
    BUTTON_CONFIRM_REGISTER = (By.NAME, "register")


class SMS_Email_Page_Locators():
    FIELD_CODE_1 = (By.ID, "rt-code-0")
    FIELD_CODE_2 = (By.ID, "rt-code-1")
    FIELD_CODE_3 = (By.ID, "rt-code-2")
    FIELD_CODE_4 = (By.ID, "rt-code-3")
    FIELD_CODE_5 = (By.ID, "rt-code-4")
    FIELD_CODE_6 = (By.ID, "rt-code-5")
    BUTTON_CHANGE_EMAIL = (By.NAME, "otp_back_phone")
    TEXT_TIMER = (By.CSS_SELECTOR, ".code-input-container__timeout")
    BITTON_SEND_NEW_CODE = (By.NAME, "otp_resend_code")
    TEXT_TITLE = (By.CSS_SELECTOR, "h1")
    TEXT_EMAIL = (By.CSS_SELECTOR, ".register-confirm-form-container__desc")


