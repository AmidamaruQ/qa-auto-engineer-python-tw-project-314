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
        element = self.element
        element.click()
        element.clear()
