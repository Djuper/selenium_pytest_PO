
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
        # messages = self.browser.find_elements(*ProductPageLocators.MESSAGE)
        # message_found = False
        # for message in messages:
        #     if text in message.text:
        #         message_found = True
        #         break
        # assert message_found, f'Messages has no contains {text}'
        how, where = ProductPageLocators.MESSAGE
        message = self.browser.find_element(how, where.format(text_message=text))
        assert text in message.text, f'Messages has no contains {text}'

    def message_should_not_be_present(self, text):
        how, where = ProductPageLocators.MESSAGE
        element_is_not_present = self.is_not_element_present(how, where.format(text_message=text))
        assert element_is_not_present, f'Message with {text} should not be present on the page'

    def message_is_disappeared(self, text):
        how, where = ProductPageLocators.MESSAGE
        message_is_disappeared = self.is_disappeared(how, where.format(text_message=text), timeout=4)
        assert message_is_disappeared, f'Message with {text} still visible on the page after 4 seconds.'

