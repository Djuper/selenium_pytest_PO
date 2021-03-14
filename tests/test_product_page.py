from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time


def test_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209' \
                       '/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.message_should_be_present(f"{product_name} has been added to your basket.")
    product_page.message_should_be_present(f"Your basket total is now {product_price}")


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_page.solve_quiz_and_get_code()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.message_should_be_present(f"{product_name} has been added to your basket.")
    product_page.message_should_be_present(f"Your basket total is now {product_price}")


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_name = product_page.get_product_name()
    product_page.message_should_not_be_present(f"{product_name} has been added to your basket.")


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_name = product_page.get_product_name()
    product_page.message_should_not_be_present(f"{product_name} has been added to your basket.")


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_add_to_basket()
    product_name = product_page.get_product_name()
    product_page.message_is_disappeared(f"{product_name} has been added to your basket.")


@pytest.mark.login
class TestLoginFromProductPage:
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.click_view_basket_button()
    basket_page = BasketPage(browser, url=browser.current_url)
    basket_page.basket_should_be_empty()


@pytest.mark.user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        login_page.open()
        login_page.register_random_new_user()
        login_page.should_be_authorized_user()
        self.product_page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
        self.product_page.open()

    def test_user_cant_see_success_message(self):
        product_name = self.product_page.get_product_name()
        self.product_page.message_should_not_be_present(f"{product_name} has been added to your basket.")

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.product_page.click_add_to_basket()
        product_name = self.product_page.get_product_name()
        product_price = self.product_page.get_product_price()
        self.product_page.message_should_be_present(f"{product_name} has been added to your basket.")
        self.product_page.message_should_be_present(f"Your basket total is now {product_price}")
