from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ALERT_ITEM_NAME = (By.CSS_SELECTOR, ".alert:nth-child(1) > .alertinner > strong")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    ALERT_ITEM_PRICE = (By.CSS_SELECTOR, ".alert > .alertinner > p:nth-child(1) > strong")
    
