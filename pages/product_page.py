from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def click_basket_button(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def check_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name = book_name.text
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET)
        book_name_in_basket = book_name_in_basket.text
        assert book_name == book_name_in_basket, "fail"

    def check_basket_cost(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = book_price.text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
        basket_cost = basket_cost.text
        assert basket_cost == book_price, "fail"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "message exists!"

    def should_not_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "message exists!"
