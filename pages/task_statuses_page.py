from selenium.webdriver.common.by import By

from pages.base_page import BasePage

ROW_WITH_CURRENT_DATA_XPATH = ("//tr[.//span[contains(text(), '{name}')] "
                               "and .//span[contains(text(), '{slug}')]]")
CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH = (ROW_WITH_CURRENT_DATA_XPATH +
                                        "//td[.//input[@type='checkbox']]")

CREATE_BUTTON_LOCATOR = (By.XPATH, "//a[@aria-label='Create']")
DELETE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Delete']")


class TaskStatusesPage(BasePage):

    @property
    def create_button(self):
        return self.button(CREATE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def _status_row(self, name, slug):
        return self.table_row((By.XPATH,
                               ROW_WITH_CURRENT_DATA_XPATH.format(name=name,
                                                                  slug=slug)))

    def _checkbox_row(self, name, slug):
        return self.input((
            By.XPATH,
            CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH.format(name=name, slug=slug)))

    def open_task_from_row(self, name, slug):
        return self._status_row(name, slug).click()

    def choose_task_from_row(self, name, slug):
        return self._checkbox_row(name, slug).click()

    def delete_chosen_task(self):
        return self.delete_button.click()

    def open_create_task(self):
        return self.create_button.click()

    def is_task_status_present(self, name, slug):
        return self._status_row(name, slug).is_present()
