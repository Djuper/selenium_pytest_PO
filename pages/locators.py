from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    HEADER = (By.XPATH, '//header')
    VIEW_BASKET_BUTTON = (By.XPATH, '//header//*[@class="btn-group"]/a')


class BasketPageLocators:
    BASKET_ITEM = (By.XPATH, '//*[@class="basket-items"]')


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FROM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    # MESSAGE = (By.CSS_SELECTOR, '[id="messages"]>div')
    MESSAGE = (By.XPATH, '//*[@id="messages"]/div[contains(., "{text_message}")]')
    PRODUCT_NAME = (By.XPATH, '//h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
