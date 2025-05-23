from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        submit_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        submit_button.click()

    def product_name_text(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price_text(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def checking_the_product_name_in_the_message(self, product_name):
        assert product_name == self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_CART).text

    def checking_the_price_sale_in_the_message(self, price):
        assert price == self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_SALE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_CART), \
            "Success message is presented, but should not be"

    def should_disappear_message(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_CART), \
            "success message not disappear"