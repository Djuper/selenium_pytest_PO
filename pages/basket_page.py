from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        basket_is_empty = self.is_not_element_present(*BasketPageLocators.BASKET_ITEM)
        assert basket_is_empty, 'There is some items in basket'

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, 'No basket in url'
