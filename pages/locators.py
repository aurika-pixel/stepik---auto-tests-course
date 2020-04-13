from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    FORM_REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    FORM_REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    FORM_REG_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REG = (By.CSS_SELECTOR, "button[name ='registration_submit']")


class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, ".alert strong")
    ADD_BASKET_TEXT = (By.CSS_SELECTOR, "")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_COST = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")


class BasketPageLocators():
    PRODUCTS_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, ".col-sm-6.h3")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner")
