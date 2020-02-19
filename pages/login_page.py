from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url  # , "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
        assert "login" in login_url, "Login_url is wrong"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        registration_form = self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM)
        # реализовал ассерт двумя способами для собственного понимания процесса
        assert registration_form, "Registration form is not presented"
