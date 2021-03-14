from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FROM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    MESSAGE = (By.CSS_SELECTOR, '[id="messages"]>div')
    PRODUCT_NAME = (By.XPATH, '//h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
