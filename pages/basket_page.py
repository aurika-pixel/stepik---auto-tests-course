from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket_message(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET_MESSAGE), "message exists!"

    def should_be_basket_is_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "message not exists!"
