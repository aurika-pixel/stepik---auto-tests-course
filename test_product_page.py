import time
import pytest
from basepage import BasePage

from pages.product_page import ProductPage


@pytest.mark.parametrize('link_promo', ["?promo=offer0", "?promo=offer1", "?promo=offer2", "?promo=offer3",
                                        "?promo=offer4", "?promo=offer5", "?promo=offer6",
                                        pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                        "?promo=offer8", "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link_promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link_promo}"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    page.solve_quiz_and_get_code()
    page.check_book_name()
    page.check_basket_cost()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    time.sleep(2)
    page.should_not_be_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
