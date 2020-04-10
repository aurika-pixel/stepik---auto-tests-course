import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:
    def test_button_add_to_basket_exists(self, browser):
        browser.get(link)
        # ожидание для визуальной проверки языка
        time.sleep(5)
        assert browser.find_element_by_css_selector("button.btn-add-to-basket")