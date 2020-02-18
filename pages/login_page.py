from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = (driver.current_url, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        assert login_url, "Login_url is wrong"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login form is not presented"

    def should_be_register_form(self):
        registration_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert registration_form, "Registration form is not presented"
