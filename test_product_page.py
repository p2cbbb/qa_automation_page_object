import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open() # открыть страницу регистрации
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "pass"
        page.register_new_user(email, password) # зарегистрировать нового пользователя
        page.should_be_authorized_user() # проверить, что пользователь залогинен

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open() # Открываем страницу товара
        page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_url()
        page.should_be_basket_button()
        page.click_button_to_add_product_into_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207" 
    page = ProductPage(browser, link)
    page.open() # Открываем страницу товара
    page.click_button_to_add_product_into_basket() # Добавляем товар в корзину 
    page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open() # Открываем страницу товара
    page.click_button_to_add_product_into_basket() # Добавляем товар в корзину
    page.should_dissapear_of_success_message() # Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open() # Гость открывает страницу товара
    page.go_to_basket_page() # Переходит в корзину по кнопке в шапке 
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items() # Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty_basket_message() # Ожидаем, что есть текст о том что корзина пуста 