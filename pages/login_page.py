from pages.base_page import BasePage
from pages.locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def fill_register_email(self, email):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)

    def fill_register_password(self, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        email_field.send_keys(password)

    def fill_register_confirm_password(self, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        email_field.send_keys(password)

    def click_register_button(self):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        email_field.click()
        self.is_disappeared(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON, timeout=20)

    def register_new_user(self, email, password):
        self.fill_register_email(email)
        self.fill_register_password(password)
        self.fill_register_confirm_password(password)
        self.click_register_button()

    def register_random_new_user(self):
        email = str(time.time()) + "@fakeemail.org"
        password = 'z_LDGkpCyHr93Y3'
        self.register_new_user(email, password)
        return email, password

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'No login in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FROM), 'Login form is not present on the page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not present on the page'
