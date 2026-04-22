from selenium.webdriver.common.by import By

from pages.base_page import BasePage

ROW_WITH_CURRENT_DATA_XPATH = "//tr[.//span[contains(text(), '{name}')]]"
CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH = (ROW_WITH_CURRENT_DATA_XPATH +
                                        "//td[.//input[@type='checkbox']]")

CREATE_BUTTON_LOCATOR = (By.XPATH, "//a[@aria-label='Create']")
DELETE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Delete']")


class LabelsPage(BasePage):

    @property
    def create_button(self):
        return self.button(CREATE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def _label_row(self, name):
        return self.table_row(
            (By.XPATH, ROW_WITH_CURRENT_DATA_XPATH.format(name=name))
        )

    def _checkbox_row(self, name):
        return self.input(
            (By.XPATH, CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH.format(name=name))
        )

    def open_label_from_row(self, name):
        return self._label_row(name).click()

    def choose_label_from_row(self, name):
        return self._checkbox_row(name).click()

    def delete_chosen_label(self):
        return self.delete_button.click()

    def open_create_label(self):
        return self.create_button.click()

    def is_label_present(self, name):
        return self._label_row(name).is_present()
