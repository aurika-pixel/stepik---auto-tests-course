from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".alert strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_COST = (By.CSS_SELECTOR, ".alertinner p strong")