from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_IS_NOT_EMPTY), \
            "Success message is not presented, basket is not empty"

    def should_be_text_basket_is_empty(self):
        t1 = self.browser.find_element(*BasePageLocators.BASKET_EMPTY).text
        print("ewrwerewrwer", t1)
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY), \
            "Missing the text 'Your basket is now empty'"
