from .web_control import WebControl
# from .web_control_test import WebControl


class TextView(WebControl):

    @property
    def text(self):
        return self._web_element.text
