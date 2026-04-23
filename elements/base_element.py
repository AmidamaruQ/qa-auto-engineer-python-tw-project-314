from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils import get_logger


class BaseElement:
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.logger = get_logger(self.__class__.__name__)

    def find_element(self):
        self.logger.info("Searching element: %s", self.locator)
        return self.driver.find_element(*self.locator)

    def find_elements(self):
        self.logger.info("Searching elements: %s", self.locator)
        return self.driver.find_elements(*self.locator)

    @property
    def element(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.locator)
        )

    @property
    def text(self):
        return self.element.text

    def is_present(self):
        for _ in range(3):
            elements = self.find_elements()

            try:
                return any(element.is_displayed() for element in elements)
            except StaleElementReferenceException:
                self.logger.info(
                    "Stale element while checking presence, retrying: %s",
                    self.locator,
                )

        return False

    def is_displayed(self):
        element = self.element
        return element.is_displayed()

    def click(self):
        self.logger.info("Clicking element: %s", self.locator)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'center'});",
            element,
        )

        try:
            element.click()
        except ElementClickInterceptedException:
            self.logger.info(
                "Native click intercepted, falling back to JavaScript: %s",
                self.locator,
            )
            self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, text):
        self.logger.info("Sending keys: %s", text)
        ActionChains(self.driver).send_keys(text)
