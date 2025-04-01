from .pages.product_page import ProductPage


def test_quest_can_add_product_to_basket(browser):
    browser.implicitly_wait(10)
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    product_name = page.product_name_text()
    product_price = page.product_price_text()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.checking_the_product_name_in_the_message(product_name)
    page.checking_the_price_sale_in_the_message(product_price)

