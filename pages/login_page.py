from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login link is not found"

    def should_be_login_form(self):
        # login_form = self.browser.find_element(*LoginPageLocators.FORM_LOGIN)
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "login form not found"

    def should_be_register_form(self):
        # registration_form = self.browser.find_element(*LoginPageLocators.FORM_REGISTRATION)
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTRATION), "registration form not found"
