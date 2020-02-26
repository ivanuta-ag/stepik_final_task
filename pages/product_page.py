from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        cart = self.browser.find_element(*ProductPageLocators.BASKET)
        cart.click()

    def should_be_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET), "Basket is not presented"

    def should_be_name_equal(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE)
        assert product_name.text == product_name_message.text, "Product name and product name message does not match"

    def should_be_price_equal(self):
        price_item = self.browser.find_element(*ProductPageLocators.PRICE_ITEM)
        price_item_message = self.browser.find_element(*ProductPageLocators.PRICE_ITEM_MESSAGE)
        assert price_item.text == price_item_message.text, "Price item and price item message does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Success message is presented, but should not be (is_not_element_present)"

    def should_not_be_success_message_by_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Success message is presented, but should not be (is_disappeared)"
