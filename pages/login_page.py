from .web_page import WebPage
from .product_page import ProductPage
from controls.button import Button
from controls.text_view import TextView
from controls.input import Input
from selenium.webdriver.common.by import By
import allure


class LoginPage(WebPage):
    APP_URL = 'https://www.saucedemo.com'

    _username_input = Input(By.ID, 'user-name')
    _pass_input = Input(By.ID, 'password')
    _login_button = Button(By.ID, 'login-button')
    _error_text = TextView(By.CSS_SELECTOR, '[data-test="error"]')

    @staticmethod
    def open(driver):
        driver.get(LoginPage.APP_URL)
        return LoginPage(driver)

    @allure.step('Log in with name: "{username}" and password: "{password}"')
    def login(self, username, password):
        return self._enter_email(username)._enter_password(password)._login()

    @allure.step('Enter username')
    def _enter_email(self, username: str):
        self._username_input.send_keys(username)
        return self

    @allure.step('Enter password')
    def _enter_password(self, password: str):
        self._pass_input.send_keys(password)
        return self

    @allure.step('Click "Login"')
    def _login(self):
        self._login_button.click()
        return ProductPage(self.driver)

    @allure.step('Get error message')
    def get_error(self):
        return self._error_text.text
