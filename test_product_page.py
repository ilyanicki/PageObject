import pytest
from .pages.product_page import ProductPage

@pytest.mark.skip
@pytest.mark.parametrize('path', ['0', '1', '2', '3', '4', '5', '6', pytest.param("7", marks=pytest.mark.xfail), '8','9'])
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

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_disappear_message()
