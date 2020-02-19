from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="id_login-username"]')
    REGISTRATION_FORM = (By.XPATH, '//*[@id="id_registration-email"]')
