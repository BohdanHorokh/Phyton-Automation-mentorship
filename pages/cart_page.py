import allure
from selenium.webdriver.common.by import By

from controls.text_view import TextView
from .web_page import WebPage


class CartPage(WebPage):
    _cart_item = TextView(By.CSS_SELECTOR, '#cart_contents_container .inventory_item_name')

    @allure.step(f'Verify if product is present in Cart')
    def is_cart_contains_product(self, product) -> bool:
        return product in [item.text for item in self._cart_item.find_all()]
