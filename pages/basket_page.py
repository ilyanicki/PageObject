from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def not_should_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM_SET)

    def should_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE)
