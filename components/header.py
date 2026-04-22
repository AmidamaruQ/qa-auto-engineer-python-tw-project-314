from selenium.webdriver.common.by import By

from components.base_components import BaseComponent
from elements import ButtonElement

PROFILE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Profile']")
HEADER_TITLE_LOCATOR = (By.XPATH, "//h6[@id='react-admin-title']")
LOGOUT_BUTTON_LOCATOR = (By.XPATH, "//span[contains(text(), 'Logout')]")


class Header(BaseComponent):
    @property
    def profile_button(self):
        return ButtonElement(self.driver, PROFILE_BUTTON_LOCATOR)

    @property
    def header_title(self):
        return self.label(HEADER_TITLE_LOCATOR)

    @property
    def logout_button(self):
        return ButtonElement(self.driver, LOGOUT_BUTTON_LOCATOR)

    def logout(self):
        self.logger.info("Logging out from header")
        self.profile_button.click()
        self.logout_button.click()
