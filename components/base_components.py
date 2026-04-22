from components.combobox import Combobox
from elements import BaseElement, ButtonElement, InputElement
from elements.table_row import TableRow
from elements.text import TextElement
from utils import get_logger


class BaseComponent:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def find(self, locator):
        self.logger.info("Finding element: %s", locator)
        return BaseElement(self.driver, locator).element

    def input(self, locator):
        self.logger.info("Building input element: %s", locator)
        return InputElement(self.driver, locator)

    def button(self, locator):
        self.logger.info("Building button element: %s", locator)
        return ButtonElement(self.driver, locator)

    def label(self, locator):
        self.logger.info("Building heading element: %s", locator)
        return TextElement(self.driver, locator)

    def table_row(self, locator):
        self.logger.info("Building table row element: %s", locator)
        return TableRow(self.driver, locator)

    def combobox(self, locator):
        self.logger.info("Building combobox element: %s", locator)
        return Combobox(self.driver, locator)
