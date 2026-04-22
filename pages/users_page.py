from selenium.webdriver.common.by import By

from pages.base_page import BasePage

CREATE_BUTTON_LOCATOR = (By.XPATH, "//a[@aria-label='Create']")
DELETE_BUTTON_LOCATOR = (By.XPATH, "//button[@aria-label='Delete']")

ROW_WITH_CURRENT_DATA_XPATH = ("//tr[.//span[contains(text(), '{email}')] "
                               "and .//span[contains(text(), '{first_name}')] "
                               "and .//span[contains(text(), '{second_name}')]]"
                               )
CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH = (ROW_WITH_CURRENT_DATA_XPATH
                                        + "//td[.//input[@type='checkbox']]")


class UsersPage(BasePage):

    @property
    def create_button(self):
        return self.button(CREATE_BUTTON_LOCATOR)

    @property
    def delete_button(self):
        return self.button(DELETE_BUTTON_LOCATOR)

    def _checkbox_user_row(self, email, first_name, second_name):
        return self.input(
            (By.XPATH, CHECKBOX_ROW_WITH_CURRENT_DATA_XPATH.format(
                email=email,
                first_name=first_name,
                second_name=second_name)))

    def _user_row(self, email, first_name, second_name):
        return self.table_row((By.XPATH, ROW_WITH_CURRENT_DATA_XPATH.format(
            email=email, first_name=first_name,
            second_name=second_name)))

    def open_create_user_form(self):
        return self.create_button.click()

    def is_user_present(self, email, first_name, second_name):
        return self._user_row(email, first_name, second_name).is_present()

    def open_user_from_table(self, email, first_name, second_name):
        return self._user_row(email, first_name, second_name).click()

    def choose_user_in_table(self, email, first_name, second_name):
        return self._checkbox_user_row(email, first_name, second_name).click()

    def delete_chosen_user(self):
        return self.delete_button.click()
