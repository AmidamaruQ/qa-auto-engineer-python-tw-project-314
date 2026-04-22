from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import xpath_literal

ROW_WITH_CURRENT_DATA_XPATH = ("//tr[.//*[normalize-space()={name}] "
                               "and .//*[normalize-space()={slug}]]")
CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH = (ROW_WITH_CURRENT_DATA_XPATH +
                                        "//td[.//input[@type='checkbox']]")

CREATE_BUTTON_LOCATOR = (By.XPATH, "//a[@aria-label='Create']")
DELETE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Delete']")
TABLE_HEADERS_LOCATOR = (By.XPATH, "//thead//th")
TABLE_ROWS_LOCATOR = (By.XPATH, "//tbody/tr")
ROW_CHECKBOXES_LOCATOR = (By.XPATH, "//tbody//input[@type='checkbox']")
ROW_WITH_NAME_XPATH = "//tr[.//*[normalize-space()={name}]]"


class TaskStatusesPage(BasePage):

    @property
    def create_button(self):
        return self.button(CREATE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def _status_row(self, name, slug):
        return self.table_row((By.XPATH,
                               ROW_WITH_CURRENT_DATA_XPATH.format(
                                   name=xpath_literal(name),
                                   slug=xpath_literal(slug),
                               )))

    def _checkbox_row(self, name, slug):
        return self.input((
            By.XPATH,
            CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH.format(
                name=xpath_literal(name),
                slug=xpath_literal(slug),
            )))

    def _status_row_by_name(self, name):
        return self.table_row((By.XPATH, ROW_WITH_NAME_XPATH.format(
            name=xpath_literal(name),
        )))

    def open_task_from_row(self, name, slug):
        return self._status_row(name, slug).click()

    def choose_task_from_row(self, name, slug):
        return self._checkbox_row(name, slug).click()

    def delete_chosen_task(self):
        return self.delete_button.click()

    def open_create_task(self):
        return self.create_button.click()

    def open_create_status(self):
        return self.open_create_task()

    def open_status_from_row(self, name, slug):
        return self.open_task_from_row(name, slug)

    def choose_status_from_row(self, name, slug):
        return self.choose_task_from_row(name, slug)

    def delete_chosen_statuses(self):
        return self.delete_chosen_task()

    def choose_all_statuses(self):
        checkboxes = self.driver.find_elements(*ROW_CHECKBOXES_LOCATOR)

        for checkbox in checkboxes:
            checkbox.click()

    def is_task_status_present(self, name, slug):
        return self._status_row(name, slug).is_present()

    def get_table_headers(self):
        return [
            header.text.strip()
            for header in self.driver.find_elements(*TABLE_HEADERS_LOCATOR)
            if header.text.strip()
        ]

    def get_statuses_count(self):
        return len(self.driver.find_elements(*TABLE_ROWS_LOCATOR))

    def get_status_row_text(self, name):
        return self._status_row_by_name(name).text
