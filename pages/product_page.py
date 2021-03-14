
from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        button = self.wait_until_element_is_clickable(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        return product_name

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def message_should_be_present(self, text):
        messages = self.browser.find_elements(*ProductPageLocators.MESSAGE)
        message_found = False
        for message in messages:
            if text in message.text:
                message_found = True
                break
        assert message_found, f'Messages has no contains {text}'
