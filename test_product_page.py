from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
# ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#          pytest.param(
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#              marks=pytest.mark.xfail),
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # print(link)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_equal()
    page.should_be_price_equal()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket()
    page.add_to_basket()
    page.should_not_be_success_message_by_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_basket_is_empty
    page.should_be_text_basket_is_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        # проверить, что         пользователь   залогинен -на этом остановился, не делал его. плюс на кнопку надо щелкнуть,на селекторе остановился

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer0/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_name_equal()
        page.should_be_price_equal()
