from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .app_driver import AppDriver


class WebControl(AppDriver):
    def __init__(self, by: By, locator: str):
        self._locator = locator
        self._by = by

    @property
    def _web_element(self):
        return WebDriverWait(self._get_driver(), 5).until(
            EC.presence_of_element_located((self._by, self._locator)))

    def is_visible(self):
        return self._web_element.is_displayed()

    def find(self, by=None, locator=None):
        strategy = by if by is not None else self._by
        locator = locator if locator is not None else self._locator
        return self._get_driver().find_element(strategy, locator)

    def find_all(self):
        return self._get_driver().find_elements(self._by, self._locator)

    def _get_driver(self):
        return self._driver
