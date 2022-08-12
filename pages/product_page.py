import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "This is not login url"

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Basket button is not presented"

    def click_button_to_add_product_into_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()

    def solve_quiz_and_check_if_correct_product_has_been_added(self):
        self.solve_quiz_and_get_code()
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        alert_item_name = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_NAME).text
        assert item_name == alert_item_name, \
        "The product name in the message does not match the product that you actually added"
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        alert_item_price = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_PRICE).text
        assert item_price == alert_item_price, "The cost of the basket does not match the price of the product"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not disappear"
    
