from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import math


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Add to basket is not presented"

    def should_be_succes_message_after_adding_item_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCES_MESSAGE), "Success message is not presented, but should be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_is_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE), \
            "Success message is presented, but should not be"

    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_correct_name_in_alert_message_after_item_add(self):
        item_name_alert_msg = self.browser.find_element(*ProductPageLocators.ITEM_NAME_ALERT_MESSAGE)
        item_name_main_title = self.browser.find_element(*ProductPageLocators.ITEM_NAME_MAIN_TITLE)
        assert item_name_main_title.text == item_name_alert_msg.text, "Item name in alert is not matching"

    def should_be_correct_price_in_alert_message_after_item_add(self):
        item_price_alert_msg = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_ALERT_MESSAGE)
        item_price_main_title = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_MAIN_TITLE)
        assert item_price_main_title.text == item_price_alert_msg.text, "Item price in alert is not matching"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
