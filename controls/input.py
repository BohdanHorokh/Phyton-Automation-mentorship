from .web_control import WebControl


class Input(WebControl):

    def send_keys(self, text):
        self._web_element.send_keys(text)

    def clear(self) -> None:
        self._web_element.clear()
