from selenium.webdriver.remote.webdriver import WebDriver


class WebPage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def driver(self):
        return self._driver
