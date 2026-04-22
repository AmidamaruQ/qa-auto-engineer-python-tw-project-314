from selenium.webdriver import Keys

from elements.base_element import BaseElement


class InputElement(BaseElement):
    def fill(self, value):
        self.logger.info("Filling input: %s", self.locator)
        self._clear_element()
        self.element.send_keys(value)

    @property
    def value(self):
        return self.element.get_attribute("value")

    def _clear_element(self):
        self.element.click()
        self.element.send_keys(Keys.COMMAND, "a")  # macOS
        self.element.send_keys(Keys.BACKSPACE)