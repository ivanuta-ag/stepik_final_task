from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="id_login-username"]')
    REGISTRATION_FORM = (By.XPATH, '//*[@id="id_registration-email"]')


class ProductPageLocators():
    BASKET = (By.XPATH, '//*[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_NAME_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_NAME = (By.XPATH, '//*[@class="col-sm-6 product_main"]/h1')
    PRICE_ITEM = (By.XPATH, '//*[@id="content_inner"]/article/div/div[2]/p[1]')
    PRICE_ITEM_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p/strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_MAIN = (By.XPATH, "//*[@id='default']/header/div/div/div[2]/span/a")
    BASKET_EMPTY = (By.XPATH, "//*[@id='content_inner']/p")
    BASKET_IS_NOT_EMPTY = (By.XPATH, "//*[@class = 'col-sm-6 h3']")
