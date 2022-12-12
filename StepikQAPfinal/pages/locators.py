from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    PAGE_URL = "https://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_FORM_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_FORM_PASS_FIELD = (By.ID, "id_registration-password1")
    REGISTER_FORM_PASS_CONFIRM_FIELD = (By.ID, "id_registration-password2")
    REGISTER_FORM_CONFIRM_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    ITEM_NAME_ALERT_MESSAGE = (
    By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in:first-of-type .alertinner strong")
    ITEM_NAME_MAIN_TITLE = (By.CSS_SELECTOR, "h1")
    ITEM_PRICE_ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    ITEM_PRICE_MAIN_TITLE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCES_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in")


class BasketPageLocators():
    PAGE_URL = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    PAGE_TITLE = (By.CSS_SELECTOR, "h1")
    ITEMS_FOR_PURCHASE = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "[id=content_inner] p")
