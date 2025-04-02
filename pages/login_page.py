from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Подстроки 'login' нет в текущем url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_FORM), "На странице не отображается форма входа"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_FORM), "На странице не отображается форма регистрации"

    def register_new_user(self, email, password):
        login_field = self.browser.find_element(*LoginPageLocators.SIGN_UP_EMAIL_FIELD)
        password_field = self.browser.find_element(*LoginPageLocators.SIGN_UP_PASSWORD_FIELD)
        repeat_password_field = self.browser.find_element(*LoginPageLocators.SIGN_UP_REPEAT_PASSWORD_FIELD)
        submit_button = self.browser.find_element(*LoginPageLocators.SIGN_UP_BUTTON)

        login_field.send_keys(email)
        password_field.send_keys(password)
        repeat_password_field.send_keys(password)
        submit_button.click()


