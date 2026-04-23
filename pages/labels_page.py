from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import xpath_literal

ROW_WITH_CURRENT_DATA_XPATH = "//tr[.//*[normalize-space()={name}]]"
CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH = (ROW_WITH_CURRENT_DATA_XPATH +
                                        "//td[.//input[@type='checkbox']]")

CREATE_BUTTON_LOCATOR = (By.XPATH, "//a[@aria-label='Create']")
DELETE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Delete']")
TABLE_HEADERS_LOCATOR = (By.XPATH, "//thead//th")
TABLE_ROWS_LOCATOR = (By.XPATH, "//tbody/tr")
ROW_CHECKBOXES_LOCATOR = (By.XPATH, "//tbody//input[@type='checkbox']")


class LabelsPage(BasePage):

    @property
    def create_button(self):
        return self.button(CREATE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def _label_row(self, name):
        return self.table_row(
            (By.XPATH, ROW_WITH_CURRENT_DATA_XPATH.format(
                name=xpath_literal(name))
             )
        )

    def _checkbox_row(self, name):
        return self.input(
            (By.XPATH, CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH.format(
                name=xpath_literal(name))
             )
        )

    def open_label_from_row(self, name):
        return self._label_row(name).click()

    def choose_label_from_row(self, name):
        return self._checkbox_row(name).click()

    def delete_chosen_label(self):
        return self.delete_button.click()

    def choose_all_labels(self):
        checkboxes = self.driver.find_elements(*ROW_CHECKBOXES_LOCATOR)

        for checkbox in checkboxes:
            self.driver.execute_script("arguments[0].click();", checkbox)

    def open_create_label(self):
        return self.create_button.click()

    def is_label_present(self, name):
        return self._label_row(name).is_present()

    def get_table_headers(self):
        return [
            header.text.strip()
            for header in self.driver.find_elements(*TABLE_HEADERS_LOCATOR)
            if header.text.strip()
        ]

    def get_labels_count(self):
        return len(self.driver.find_elements(*TABLE_ROWS_LOCATOR))

    def get_rows_text(self):
        return [
            row.text.strip()
            for row in self.driver.find_elements(*TABLE_ROWS_LOCATOR)
            if row.text.strip()
        ]
