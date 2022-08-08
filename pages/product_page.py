import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_basket_button()
        self.add_to_basket_and_check_if_correct_product_was_been_added()

    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "This is not login url"

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Basket button is not presented"

    def add_to_basket_and_check_if_correct_product_was_been_added(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()
        self.solve_quiz_and_get_code()
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        alert_item_name = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_NAME).text
        assert item_name == alert_item_name, "The product name in the message does not match the product that you actually added"
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        alert_item_price = self.browser.find_element(*ProductPageLocators.ALERT_ITEM_PRICE).text
        assert item_price == alert_item_price, "The cost of the basket does not match the price of the product"

