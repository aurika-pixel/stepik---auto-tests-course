from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def click_basket_button(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_basket.click()

    def check_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name = book_name.text
        assert "The shellcoder's handbook" in book_name, "fail"

    def check_basket_cost(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        book_price = book_price.text
        basket_cost = self.browser.find_element(*ProductPageLocators.BASKET_COST)
        basket_cost = basket_cost.text
        assert basket_cost in book_price, "fail"
