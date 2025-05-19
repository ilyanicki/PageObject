import pytest
from faker import Faker
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.need_review
@pytest.mark.parametrize('path', ['6', pytest.param("7", marks=pytest.mark.xfail), '8','9'])
def test_quest_can_add_product_to_basket(browser, path):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer" + path
    page = ProductPage(browser, link)
    page.open()
    product_name = page.product_name_text()
    product_price = page.product_price_text()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.checking_the_product_name_in_the_message(product_name)
    page.checking_the_price_sale_in_the_message(product_price)

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

#@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_disappear_message()


def test_guest_should_see_login_link_on_product_page(browser):
    browser.implicitly_wait(5)
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    browser.implicitly_wait(5)
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.not_should_be_products()
    basket_page.should_message_basket_is_empty()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.implicitly_wait(5)
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        fake = Faker()
        email_value = fake.email()
        password_value = fake.password(length=12)
        page.register_new_user(email_value, password_value)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self,browser):
        browser.implicitly_wait(10)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        product_name = page.product_name_text()
        product_price = page.product_price_text()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.checking_the_product_name_in_the_message(product_name)
        page.checking_the_price_sale_in_the_message(product_price)




