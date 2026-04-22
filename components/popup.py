from selenium.webdriver.common.by import By

from components.base_components import BaseComponent
from utils.utils import wait_for

POPUP_TITLE_LOCATOR = "//div[@role='alert']/div[contains(text(), '{text}')]"
ANY_POPUP_TITLE_LOCATOR = (By.XPATH, "//div[@role='alert']/div")


class Popup(BaseComponent):

    def popup_label_with_text(self, text):
        return self.label((By.XPATH, POPUP_TITLE_LOCATOR.format(text=text)))

    def wait_popup_with_text(self, text):
        return wait_for(lambda: self.popup_label_with_text(text).is_present())

    @property
    def text(self):
        return self.label(ANY_POPUP_TITLE_LOCATOR).text
