# from .web_control_test import WebControl
from .web_control import WebControl


class Button(WebControl):

    def click(self):
        self._web_element.click()
